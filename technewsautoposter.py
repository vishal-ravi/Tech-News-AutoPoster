import requests
from pymongo import MongoClient
from datetime import datetime, timedelta
import time

# Configuration
NEWS_API_KEY = 'your_news_api_key'
DEV_TO_API_KEY = 'your_dev_to_api_key'
MONGO_URI = 'mongodb+srv://<username>:<password>@news.zla8zxf.mongodb.net/?retryWrites=true&w=majority&appName=news'
DB_NAME = 'technews'
COLLECTION_NAME = 'technology_news'
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'

# Rate limit configuration
RATE_LIMIT = 10  # Number of requests per minute
DELAY = 60 / RATE_LIMIT  # Delay between requests in seconds

# MongoDB client setup
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Fetch technology news from NewsAPI
def fetch_technology_news(api_key, from_date, to_date):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': api_key,
        'q': 'technology',
        'from': from_date,
        'to': to_date,
        'language': 'en',
        'pageSize': 100
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Insert data into MongoDB
def insert_into_mongodb(articles):
    for article in articles:
        document = {
            'author': article.get('author'),
            'title': article.get('title'),
            'description': article.get('description'),
            'url': article.get('url'),
            'urlToImage': article.get('urlToImage'),
            'content': article.get('content'),
            'publishedAt': article.get('publishedAt'),
            'fetchedAt': datetime.utcnow()
        }
        collection.update_one({'url': article.get('url')}, {'$set': document}, upsert=True)

# Post news article to Dev.to
def post_to_dev_to(api_key, article):
    url = 'https://dev.to/api/articles'
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'article': {
            'title': article['title'],
            'published': True,
            'body_markdown': article['content'],
            'tags': ['technology', 'news']
        }
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Successfully posted article: {article['title']}")
    elif response.status_code == 429:
        print(f"Rate limit reached, retrying after delay: {response.status_code}")
        time.sleep(DELAY)
        post_to_dev_to(api_key, article)  # Retry posting the article
    else:
        print(f"Failed to post article: {response.status_code}")

# Main function to fetch, insert, and post articles
def main():
    now = datetime.utcnow()
    last_update = collection.find_one(sort=[('fetchedAt', -1)])
    if last_update:
        last_update_time = last_update['fetchedAt']
        next_update_time = last_update_time + timedelta(days=1)
        if now < next_update_time:
            print("Less than 24 hours since last update. Skipping fetch.")
            return

    start_date = (now - timedelta(days=1)).strftime('%Y-%m-%d')
    end_date = now.strftime('%Y-%m-%d')
    
    data = fetch_technology_news(NEWS_API_KEY, start_date, end_date)
    if data and data.get('status') == 'ok':
        articles = data.get('articles', [])
        insert_into_mongodb(articles)
        print(f"Inserted {len(articles)} articles into MongoDB.")
        
        for article in articles:
            post_to_dev_to(DEV_TO_API_KEY, article)
            time.sleep(DELAY)  # Delay between each post to avoid hitting rate limits
    else:
        print("No data found or error in fetching data.")

if __name__ == "__main__":
    main()

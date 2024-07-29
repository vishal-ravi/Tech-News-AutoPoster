# Tech News AutoPoster

Welcome to the Tech News AutoPoster repository! This project is an innovative solution for automating the fetching, storing, and posting of technology news articles. The system fetches the latest technology news using NewsAPI, stores them in a MongoDB database, and posts them to Dev.to, ensuring a constant flow of fresh tech content.

## Features

- **Automated News Fetching**: Fetches the latest technology news articles from NewsAPI.
- **MongoDB Integration**: Stores fetched news articles in a MongoDB database for easy retrieval and management.
- **Automated Posting to Dev.to**: Posts the stored news articles to Dev.to, ensuring your tech blog is always up-to-date.
- **Rate Limiting Handling**: Manages rate limits to comply with API usage policies, retrying requests as needed.

## Getting Started

Follow these steps to set up and run the Tech News AutoPoster.

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account
- Dev.to account

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/tech-news-autoposter.git
    cd tech-news-autoposter
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```


### Obtaining API Keys

#### NewsAPI

To obtain a NewsAPI API key, follow these steps:
1. Go to the [NewsAPI website](https://newsapi.org/) and sign up for an account.
2. Once you have signed up and logged in, navigate to your account settings.
3. In the account settings, generate a new API key.
4. Copy the generated API key and securely store it in your `.env` file.

#### Dev.to

To obtain a Dev.to API key, follow these steps:
1. Log in to your [Dev.to](https://dev.to/) account.
2. Navigate to your account settings.
3. In the API section, generate a new API key.
4. Copy the API key and securely store it in your `.env` file.

### Setting Up MongoDB

1. **Create a MongoDB Atlas Account**: Sign up for a free MongoDB Atlas account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. **Create a Cluster**: Follow the instructions to create a new cluster.
3. **Whitelist IP Address**: In the Network Access settings, add your IP address or `0.0.0.0/0` for open access.
4. **Create a Database User**: In the Database Access settings, create a new user with read and write privileges.
5. **Get Connection String**: Go to the Clusters section, click "Connect", and choose "Connect your application" to get the connection string. Replace `<username>`, `<password>`, and `<dbname>` in the string.

### Running the Project

1. **Activate Virtual Environment**:
    ```sh
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

2. **Run the Main Script**:
    ```sh
    python main.py
    ```

This will start the automation process, fetching news articles, storing them in MongoDB, and posting them to Dev.to.

## Contributing

We welcome contributions! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

By following this guide, you'll have the Tech News AutoPoster up and running, automating the process of fetching, storing, and posting technology news articles, making it an essential tool for tech bloggers and news enthusiasts.
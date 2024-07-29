# Setting Up MongoDB for Tech News AutoPoster

This guide will walk you through the steps to set up MongoDB for the Tech News AutoPoster project. MongoDB will be used to store fetched technology news articles before they are posted to Dev.to.

## Prerequisites

1. **MongoDB Atlas Account**: Sign up for a free MongoDB Atlas account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. **MongoDB Atlas Cluster**: Create a cluster in your MongoDB Atlas account.
3. **MongoDB Compass** (Optional): Download and install MongoDB Compass for a GUI to interact with your MongoDB database.

## Step-by-Step Setup

### 1. Create a MongoDB Atlas Cluster

1. **Sign In**: Log in to your MongoDB Atlas account.
2. **Create a Cluster**: Follow the instructions to create a new cluster. Choose the free tier for testing purposes.
3. **Configure Cluster**:
    - **Cloud Provider & Region**: Choose a cloud provider and region.
    - **Cluster Tier**: Select the free M0 tier.
    - **Cluster Name**: Give your cluster a name.
    - **Additional Settings**: Leave the defaults for additional settings.

4. **Create Cluster**: Click the "Create Cluster" button.

### 2. Whitelist IP Address

1. **Network Access**: Navigate to "Network Access" in the left-hand menu.
2. **Add IP Address**: Click "Add IP Address" and add your IP address. You can add `0.0.0.0/0` to allow access from anywhere, but this is not recommended for production.

### 3. Create a Database User

1. **Database Access**: Navigate to "Database Access" in the left-hand menu.
2. **Add New Database User**: Click "Add New Database User" and fill out the form.
    - **Username**: Choose a username.
    - **Password**: Choose a secure password.
    - **Database User Privileges**: Select "Read and write to any database" for simplicity.
3. **Add User**: Click the "Add User" button.

### 4. Connect to Your Cluster

1. **Clusters**: Go back to the "Clusters" tab.
2. **Connect**: Click the "Connect" button on your cluster.
3. **Connection Method**: Choose "Connect your application."
4. **Connection String**: Copy the connection string provided. It will look something like this:
    ```
    mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<dbname>?retryWrites=true&w=majority
    ```


### 5. Verify Connection (Optional)

You can use MongoDB Compass to verify the connection and view your database.

1. **Open MongoDB Compass**: Launch MongoDB Compass.
2. **New Connection**: Click "New Connection" and paste your connection string.
3. **Connect**: Click the "Connect" button to connect to your cluster.
4. **View Database**: You should now be able to see your database and collections.

## Final Steps

With MongoDB set up and your `.env` file configured, you are now ready to run the Tech News AutoPoster script and start fetching and storing technology news articles.

```sh
# Activate your virtual environment
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

# Run the main script
python main.py
```

This will start the automation process, fetching news articles and storing them in your MongoDB database.

## Troubleshooting

- **Connection Errors**: Double-check your connection string, username, password, and cluster name.
- **IP Whitelist**: Ensure your IP address is whitelisted in the MongoDB Atlas Network Access settings.
- **Database User Privileges**: Make sure your database user has the correct privileges.

With MongoDB properly set up, your Tech News AutoPoster should work seamlessly, automating the fetching and posting of technology news.
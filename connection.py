"""
This python file explains how to establish connection with the MongoDB server
username and password are stored in environment file for security purpose
URI can be retrieved from "Connect" option in MongoDB Cluster on cloud
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
username, password = os.getenv("MY_MDB_ORG_USER"), os.getenv("MY_MDB_ORG_PASSWORD")
MONGODB_uri = f"mongodb+srv://{username}:{password}@myatlasclusteredu.bcqr7.mongodb.net/?retryWrites=true&w=majority&appName=myAtlasClusterEDU"
MONGODB_URI = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Get list of database names
for db_name in client.list_database_names():
    print(db_name)

# Always close the client after completing the operation
client.close()


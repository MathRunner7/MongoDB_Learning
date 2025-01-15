"""
This python file shows an example of updating single and multiple documents into MongoDB collections
Refer connection.py to understand how connection is established

collection.update_one() updates first document that matches a query
collection.update_many() updates all documents that matches a query
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import pprint

# Import ObjectID from bson package (part of PyMongo distribution) to enable querying by ObjectID
from bson.objectid import ObjectId

load_dotenv()
username, password = os.getenv("MY_MDB_ORG_USER"), os.getenv("MY_MDB_ORG_PASSWORD")
MONGODB_uri = f"mongodb+srv://{username}:{password}@myatlasclusteredu.bcqr7.mongodb.net/?retryWrites=true&w=majority&appName=myAtlasClusterEDU"
MONGODB_URI = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
# Get reference to 'sample_guides' Database and 'planets' collection
db = client.sample_guides
planet_collection = db.planets

client.close()

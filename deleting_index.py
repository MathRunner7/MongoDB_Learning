"""
This python file shows an example of deleting index on MongoDB collections
Refer connection.py to understand how connection is established

collection.hide_index() hides an index
collection.drop_index() drops one index
collection.drop_indexes() drops all indexes

MONGODB_URI is a connection string which can be retrieved from connect button in cluster at MongoDB Atlas
"""
from pymongo import IndexModel, ASCENDING, DESCENDING
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import pprint

# Import ObjectID from bson package (part of PyMongo distribution) to enable querying by ObjectID
from bson.objectid import ObjectId

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
# Get reference to 'sample_guides' Database and 'planets' collection
db = client.sample_guides
collection = db.planets

# Define indexes
index_to_delete = 'name_1'
result = collection.drop_index(index_to_delete)
print('Following index is deleted: ', index_to_delete)

print('Remaining indexes are:')
for each in collection.list_indexes():
    print(each)

result = collection.drop_indexes()
print('All indexes are deleted.')

# Always close the client after completing the operation
client.close()
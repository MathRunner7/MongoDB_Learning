"""
This python file shows an example of creating compound index on MongoDB collections
Refer connection.py to understand how connection is established

collection.create_indexes() creates multiple indexes
collection.list_indexes() returns list of indexes

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
db = client.sample_training
collection = db.routes

# Define indexes
index1 = IndexModel([('src_airport', ASCENDING), ('dst_airport', DESCENDING)])
index2 = IndexModel([('airline.name', ASCENDING)])
# Create a multi field compound Index
result = collection.create_indexes([index1, index2])
print('Following index is created: ', result)

for each in collection.list_indexes():
    print(each)

print('='*100)
print('Querying through single field index')
pprint.pprint(collection.find({'src_airport': 'BTK'}).sort({'dst_airport':1}).explain())
print('='*100)
print('Querying through multikey index')
pprint.pprint(collection.find({'airline.name': 'Cargoitalia'}).explain())

# Always close the client after completing the operation
client.close()
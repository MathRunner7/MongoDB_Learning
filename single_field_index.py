"""
This python file shows an example of creating single field index on MongoDB collections
Refer connection.py to understand how connection is established

collection.create_index() creates single field index
collection.list_indexes() returns list of indexes

MONGODB_URI is a connection string which can be retrieved from connect button in cluster at MongoDB Atlas
"""
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

# Define single field index
single_field_index = {'hasRings': 1}
single_field_unique_index = {'name': 1}
# Create a single field Index
result = collection.create_index(single_field_index)
print('Following index is created: ', result)
result = collection.create_index(single_field_unique_index, unique=True)
print('Following unique index is created: ', result)

# Create a multi key Index on array field
multikey_index = {'mainAtmosphere': 1}
result = collection.create_index(multikey_index)
print('Following multikey index is created: ', result)

for each in collection.list_indexes():
    print(each)

print('='*100)
print('Querying through single field index')
pprint.pprint(collection.find({'name': 'Mars'}).explain())
print('='*100)
print('Querying through multikey index')
pprint.pprint(collection.find({'mainAtmosphere': 'CH4'}).explain())
# Always close the client after completing the operation
client.close()
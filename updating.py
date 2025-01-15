"""
This python file shows an example of updating single and multiple documents into MongoDB collections
Refer connection.py to understand how connection is established

collection.update_one() updates first document that matches a query
collection.update_many() updates all documents that matches a query

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
planet_collection = db.planets

# Filter document
document_to_find = {'_id': ObjectId('621ff30d2a3e781873fcb660')}
# Update document
document_to_update = {'$set':{'hasRings': True}}
# Updating single document
result = planet_collection.update_one(document_to_find, document_to_update)
print('Document Updated: ', result.modified_count)
pprint.pprint(planet_collection.find_one(document_to_find))

# Filter document
document_to_find = {'orderFromSun': {'$gte':5}}
# Update document
document_to_update = {'$set':{'state': 'Gas'}}
# Updating multiple document
result = planet_collection.update_many(document_to_find, document_to_update)
print('Document Matched: ', result.matched_count)
print('Document Updated: ', result.modified_count)

# Filter document
document_to_find = {'orderFromSun': {'$lt':5}}
# Update document
document_to_update = {'$set':{'state': 'Solid'}}
# Updating multiple document
result = planet_collection.update_many(document_to_find, document_to_update)
print('Document Matched: ', result.matched_count)
print('Document Updated: ', result.modified_count)

client.close()


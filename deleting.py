"""
This python file shows an example of deleting single and multiple documents from MongoDB collections
Refer connection.py to understand how connection is established

collection.delete_one() deletes first document that matches a query
collection.delete_many() deletes all matching documents
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

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

# Deleting Single Document
# Query by ObjectID
document_to_delete = {'_id': ObjectId('6784f7d5943726199efc504a')}
result = planet_collection.delete_one(document_to_delete)
print('Documents Deleted: ', result.deleted_count)
# Query by field names
document_to_delete = {'name': 'Pluto'}
result = planet_collection.delete_one(document_to_delete)
print('Documents Deleted: ', result.deleted_count)

# Deleting Multiple Document
# Query by ObjectID
document_to_delete = {'name': {'$in':['Orcus','Ceres','Pluto']}}
result = planet_collection.delete_many(document_to_delete)
print('Documents Deleted: ', result.deleted_count)

client.close()

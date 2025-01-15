"""
This python file shows an example of querying single and multiple documents from MongoDB collections
Refer connection.py to understand how connection is established

collection.find_one() returns first document that matches a query or None if there are no matches
collection.find() returns a cursor instance which allows to iterate over all matching documents
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

# Querying Single Document
#Query by ObjectID
document_to_find = {'_id': ObjectId('621ff30d2a3e781873fcb660')}
result = planet_collection.find_one(document_to_find)
pprint.pprint(result)

#Query by ObjectID
document_to_find = {'name': 'Mars'}
result = planet_collection.find_one(document_to_find)
pprint.pprint(result)

# Querying Multiple Documents
document_to_find = {'hasRings': True}
result = planet_collection.find(document_to_find)

found_planets = 0
for planet in result:
    found_planets += 1
    pprint.pprint(planet)

print(f'Total {found_planets} found in this query')

client.close()
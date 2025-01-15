"""
This python file shows an example of inserting single and multiple documents into MongoDB collections
Refer connection.py to understand how connection is established

collection.insert_one(document) adds single document to the referred collection,
collection.insert_many([document1, document2, ...]) adds multiple document to the referred collection
Both the method returns the ObjectID or list of ObjectIDs for successfully added documents

MONGODB_URI is a connection string which can be retrieved from connect button in cluster at MongoDB Atlas
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
# Get reference to 'sample_guides' Database
db = client.sample_guides
# Get reference to 'planets' collection
planet_collection = db.planets

# Assign document in form of dictionary to a variable
new_single_planet = {
  "name": "Pluto",
  "orderFromSun": 9,
  "hasRings": False,
  "mainAtmosphere": ["N2", "CH4", "CO"],
  "surfaceTemperatureC": {"min": -240.00, "max": -218.00, "mean": -229.00}
}

result = planet_collection.insert_one(new_single_planet)
document_id = result.inserted_id
print(f"_id of inserted single document is: {document_id}")

# Assign multiple document in form of list of dictionaries to a variable
new_many_planet = [
    {
        "name": "Ceres",
        "orderFromSun": 4.5,
        "hasRings": False,
        "mainAtmosphere": ["H2O"],
        "surfaceTemperatureC": {"min": -163.15, "max": -38.15, "mean": -100.65}
    },
    {
        "name": "Orcus",
        "orderFromSun": 9.5,
        "hasRings": False,
        "mainAtmosphere": ["NA"],
        "surfaceTemperatureC": {"min": None, "max": None, "mean": None}
    },
]

result = planet_collection.insert_many(new_many_planet)
document_id = result.inserted_ids
for _id in document_id:
    print(f"_id of inserted document is: {_id}")

# Always close the client after completing the operation
client.close()

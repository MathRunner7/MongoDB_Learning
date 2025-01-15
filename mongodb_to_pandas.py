"""
This python file shows an example of how to convert MongoDB dataset to Pandas Dataframe
For this task PyMongoArrow standard package is used

MONGODB_URI is a connection string which can be retrieved from connect button in cluster at MongoDB Atlas
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongoarrow.monkey import patch_all
from dotenv import load_dotenv
import pandas as pd
import numpy as np
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
patch_all()
# Standard method to fetch MongoDB collection into Pandas Dataframe is <collection>.find_pandas_all(<filter_query>, schema=defined_schema)
df = planet_collection.find_pandas_all({}) # {} is an empty filter which will return all the documents from collection
print(df)
""" Expected Output Example:
                        _id     name  orderFromSun  hasRings      mainAtmosphere                          surfaceTemperatureC  state
0  621ff30d2a3e781873fcb663   Saturn             6      True  [H2, He, CH4, NH3]  {'min': None, 'max': None, 'mean': -139.15}    Gas
1  621ff30d2a3e781873fcb65f  Neptune             8      True       [H2, He, CH4]   {'min': None, 'max': None, 'mean': -201.0}    Gas
2  621ff30d2a3e781873fcb662    Venus             2     False            [CO2, N]    {'min': None, 'max': None, 'mean': 464.0}  Solid
3  621ff30d2a3e781873fcb65d   Uranus             7      True       [H2, He, CH4]   {'min': None, 'max': None, 'mean': -197.2}    Gas
4  621ff30d2a3e781873fcb65c  Mercury             1     False                  []  {'min': -173.0, 'max': 427.0, 'mean': 67.0}  Solid
5  621ff30d2a3e781873fcb661    Earth             3     False         [N, O2, Ar]    {'min': -89.0, 'max': 56.0, 'mean': 14.0}  Solid
6  621ff30d2a3e781873fcb65e     Mars             4     False        [CO2, Ar, N]  {'min': -143.0, 'max': 35.0, 'mean': -63.0}  Solid
7  621ff30d2a3e781873fcb660  Jupiter             5      True       [H2, He, CH4]  {'min': None, 'max': None, 'mean': -145.15}    Gas
"""
# Always close the client after completing the operation
client.close()

import os
import sys
from pymongo import MongoClient
from pprint import pprint

# Connecting to MongoDB host and port 
client = MongoClient('mongodb://localhost:27017/')
db = client.MakeSchool
collections = db.students



pprint("MONGODB - A collection oriented database")
print"Collections : {}".format(db.command(collections))


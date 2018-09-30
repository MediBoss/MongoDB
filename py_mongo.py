import os
import sys
from pymongo import MongoClient
from pprint import pprint

client = MongoClient(<MONGODB URL>)
db = client.admin

serverStatusResults = db.command("serverStatus")
pprint(serverStatus)

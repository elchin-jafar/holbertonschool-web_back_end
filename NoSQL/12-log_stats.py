#!/usr/bin/env python3
"""represent some logs nginx"""

from pymongo import MongoClient


client = MongoClient(host="localhost", port=27017)

db = client.holberton

collection = db.holberton

count = collection.count_documents({})

print("{} logs".format(count))
print("Methods:")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

for method in methods:
    docs = collection.find({"method": method})
    print("method {}: {}".format(method, len(docs)))

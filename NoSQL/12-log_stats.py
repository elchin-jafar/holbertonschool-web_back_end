#!/usr/bin/env python3
"""represent some logs nginx"""

from pymongo import MongoClient


if __name__ == "__main__":
    """main"""
    client = MongoClient(host="localhost", port=27017)

    db = client.logs

    collection = db.nginx

    count = collection.count_documents({})

    print("{} logs".format(count))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print("method {}: {}".format(method, count))

    countGet = collection.count_documents({"method": "GET", "path": "/status"})

    print("{} status check".format(countGet))

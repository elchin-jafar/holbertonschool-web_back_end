#!/usr/bin/env python3
"""list all documents in given collection"""


def list_all(mongo_collection):
    """list all documents in given collection"""
    if not mongo_collection.find():
        return []
    return mongo_collection.find()

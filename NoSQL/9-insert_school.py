#!/usr/bin/env python3
"""insert a document in python"""


def insert_school(mongo_collection, **kwargs):
    """insert given data to collection based on kwargs"""
    result = mongo_collection.insert(kwargs)
    return result

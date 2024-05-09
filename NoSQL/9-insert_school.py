#!/usr/bin/env python3
"""insert a document in python"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert given data to collection based on kwargs"""
    return db.mongo_collection.insert(kwargs)

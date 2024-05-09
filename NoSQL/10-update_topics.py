#!/usr/bin/env python3
"""update data"""


def update_topics(mongo_collection, name, topics):
    """change all topics of a school document based on the name"""
    mongo_collection.update({"name": name}, {$set: {"topics": topics}}, {multi: true})

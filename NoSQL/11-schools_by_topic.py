#!/usr/bin/env python3
"""list schools which have same topics"""


def schools_by_topic(mongo_collection, topic):
    """find and return same topic schools"""
    return mongo_collection.find({"topic": topic})

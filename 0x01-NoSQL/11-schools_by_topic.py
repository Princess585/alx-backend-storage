#!/usr/bin/env python3
"""Function that returns the list of school topics"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school topics"""
    collection = mongo_collection.find({"topics": topic})
    return collection

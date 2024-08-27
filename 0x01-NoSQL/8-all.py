#!/usr/bin/env python3
"""
Python function that lists all docs in a collection
"""


def list_all(mongo_collection):
    """
    Return an empty list if no doc in the collection
    """
    return list(mongo_collection.find())

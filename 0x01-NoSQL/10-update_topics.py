#!/usr/bin/env python3
"""Function that changes all topics of a school doc"""


def update_topics(mongo_collection, name, topics):
    """Lists of strings"""
    filter = {"name": name}
    update_document = {"$set": {"topics": topics}}

    mongo_collection.update_many(filter, update_document)

#!/usr/bin/env python3
"""Function that returns all students sorted by ave score"""

from pymongo import MongoClient

def top_students(mongo_collection):
    """Returns all students"""
    pipeline = [
        {
            "$unwind": "$scores"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    
    results = list(mongo_collection.aggregate(pipeline))
    
    return results

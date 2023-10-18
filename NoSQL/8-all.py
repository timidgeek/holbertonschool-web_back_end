#!/usr/bin/env python3
"""task eight, mongo list"""
import pymongo


def list_all(mongo_collection):
    """
    list all documents in a `mongodb` collection
    if empty collection, return empty list
    """
    return list(mongo_collection.find())

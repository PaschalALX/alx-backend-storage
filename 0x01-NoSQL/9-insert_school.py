#!/usr/bin/env python3
""" Task 9 - Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection  """

    return mongo_collection.insert_one(kwargs)

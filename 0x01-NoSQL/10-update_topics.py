#!/usr/bin/env python3
""" Task 10 - Change School Topics """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document  """

    filter_query = {"name": name}
    update_value = {"$set": {"topics": topic}}

    mongo_collection.update(filter_query, update_value)

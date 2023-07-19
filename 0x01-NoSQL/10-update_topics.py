#!/usr/bin/env python3
""" Task 10 - Change School Topics """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document  """

    mongo_collection.update({"name": name}, {
        "$set": {
            "topics": topics
        }
    }, "multi": true)

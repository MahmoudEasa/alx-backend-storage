#!/usr/bin/env python3
""" Returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Schools by Topic Function """
    return (mongo_collection.find({"topics": {"$in": [topic]}}))

#!/usr/bin/env python3
""" Changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ Update Topics Function """
    try:
        mongo_collection.update_one({"name": name},
                                    {"$set": {"topics": topics}})
    except Exception as ex:
        print(str(ex))

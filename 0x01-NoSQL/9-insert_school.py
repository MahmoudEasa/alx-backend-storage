#!/usr/bin/env python3
""" Inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Insert School Function """
    try:
        result = mongo_collection.insert_one(kwargs)
        return (result.inserted_id)
    except Exception as ex:
        print(str(ex))

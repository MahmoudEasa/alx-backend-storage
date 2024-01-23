#!/usr/bin/env python3
""" lists all documents in a collection """


def list_all(mongo_collection):
    """ List All Function """
    return (mongo_collection.find())

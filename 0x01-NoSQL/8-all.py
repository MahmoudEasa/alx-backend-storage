#!/usr/bin/env python3
""" lists all documents in a collection """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ List All Function """
    db = mongo_collection
    return (db.find())

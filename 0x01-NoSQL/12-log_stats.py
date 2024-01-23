#!/usr/bin/env python3
""" Python script that provides some stats
    about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def provides_stats():
    """ Provides Stats Function """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    print(f"{db.count_documents({})} logs")
    print("Methods:")

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:
        print(f"\tmethod {method}: {db.count_documents({'method': method})}")

    status_get = db.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_get} status check")


if __name__ == "__main__":
    provides_stats()

#!/usr/bin/env python3
""" Python script that provides some stats
    about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def provides_stats():
    """ Provides Stats Function """
    client = MongoClient('mongodb://127.0.0.1:27017')

    db = client.logs.nginx
    x = db.count_documents({})
    get = db.count_documents({'method': 'GET'})
    post = db.count_documents({'method': 'POST'})
    put = db.count_documents({'method': 'PUT'})
    patch = db.count_documents({'method': 'PATCH'})
    delete = db.count_documents({'method': 'DELETE'})
    status_get = db.count_documents({'method': 'GET', 'path': '/status'})
    data = f"""{x} logs
Methods:
    method GET: {get}
    method POST: {post}
    method PUT: {put}
    method PATCH: {patch}
    method DELETE: {delete}
{status_get} status check"""
    print(data)


if __name__ == "__main__":
    provides_stats()

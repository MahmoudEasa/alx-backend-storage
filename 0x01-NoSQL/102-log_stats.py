#!/usr/bin/env python3
""" Improve 12-log_stats.py by adding the top 10 of the most present
    IPs in the collection nginx of the database logs
"""
from pymongo import MongoClient
from collections import Counter


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
    print("IPs:")

    all_data = db.find()
    ip_counts = Counter(obj['ip'] for obj in all_data)
    sorted_counts = sorted(
            ip_counts.items(), key=lambda obj: obj[1], reverse=True
    )
    loop_count = 0

    for ip, count in sorted_counts:
        loop_count += 1
        print(f"\t{ip}: {count}")
        if loop_count == 10:
            break


if __name__ == "__main__":
    provides_stats()

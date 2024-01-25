#!/usr/bin/env python3
""" Uses the requests module to obtain the HTML content of
    a particular URL and returns it
"""
import requests
import redis
from functools import wraps
from typing import Callable

r = redis.Redis()


def cache_count(method: Callable) -> Callable:
    """ Cache Count Decorator """
    @wraps(method)
    def wrapper(url: str):
        """ Wrapper Function """
        count_key = f"count:{url}"
        cached = r.get(url)

        if cached:
            r.incr(count_key)
            return (cached.decode('utf-8'))

        content = method(url)
        r.setex(url, 10, content)
        r.incr(count_key)
        return (content)

    return (wrapper)


@cache_count
def get_page(url: str) -> str:
    """ Get Page Function """
    res = requests.get(url).text
    return (res)

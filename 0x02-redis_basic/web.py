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
    @wraps(method, *args, **kwargs)
    def wrapper(url: str) -> str:
        """ Wrapper Function """
        count_key = f"count:{url}"
        cached_url = f"cached:{url}"
        cached = r.get(cached_url)

        if cached:
            r.incr(count_key)
            return (cached.decode('utf-8'))

        content = method(url, *args, **kwargs)
        r.setex(cached_url, 10, content)
        r.set(count_key, 0)
        return (content)

    return (wrapper)


@cache_count
def get_page(url: str) -> str:
    """ Get Page Function """
    try:
        res = requests.get(url).text
        return (res)
    except requests.RequestException as e:
        return ("")

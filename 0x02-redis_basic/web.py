#!/usr/bin/env python3
""" Uses the requests module to obtain the HTML content of
    a particular URL and returns it
"""
import requests
import redis
from functools import wraps
from typing import Callable
import time

r = redis.Redis()
r.flushdb()


def cache_count(method: Callable) -> Callable:
    """ Cache Count Decorator """
    @wraps(method)
    def wrapper(url: str) -> str:
        """ Wrapper Function """
        count_key = f"count:{url}"
        cached_url = f"cached:{url}"
        cached = r.get(cached_url)

        if cached:
            r.incr(count_key)
            return (cached.decode('utf-8'))

        content = method(url)
        r.setex(cached_url, 10, content)
        r.set(count_key, 1)
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


url = "http://slowwly.robertomurray.co.uk"
get_page(url)
get_page(url)
get_page(url)
get_page(url)
get_page(url)
get_page(url)
get_page(url)
get_page(url)
get_page(url)
print(r.get(f"count:{url}"))
print(r.get(f"cached:{url}"))

time.sleep(11)
print(r.get(f"count:{url}"))
print(r.get(f"cached:{url}"))

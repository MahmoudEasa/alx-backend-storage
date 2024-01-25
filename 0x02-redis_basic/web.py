#!/usr/bin/env python3
""" Uses the requests module to obtain the HTML content of
    a particular URL and returns it
"""
import requests
import redis
from functools import wraps
from typing import Callable

r = redis.Redis()
r.flushdb()


def cache_count(method: Callable) -> Callable:
    """ Cache Count Decorator """
    @wraps(method)
    def wrapper(url: str) -> str:
        """ Wrapper Function """
        count_key = f"count:{url}"
        cached = r.get(count_key)

        try:
            content = method(url)
        except requests.RequestException as e:
            return ("")

        if not cached:
            r.setex(url, 10, content)

        r.incr(count_key)
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


if __name__ == "__main__":
    get_page("http://google.com")

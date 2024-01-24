#!/usr/bin/env python3
""" Create a Cache class. In the __init__ method,
    store an instance of the Redis client as a private
    variable named _redis (using redis.Redis())
    and flush the instance using flushdb
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count Calls Decorator takes a single method Callable
        argument and returns a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper Function increments the count for
            that key every time the method is called
        """
        self._redis.incr(key)
        return (method(self, *args, **kwargs))

    return (wrapper)


class Cache:
    """ Cache class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store Method """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return (random_key)

    def get(self, key: str, fn: Callable = None):
        """ Get Method """
        data = self._redis.get(str(key))
        if fn:
            data = fn(data)

        return (data)

    def get_str(self, key: str) -> str:
        """ Get Str Method """
        return (self.get(key, fn=lambda x: x.decode("utf-8")))

    def get_int(self, key: str) -> int:
        """ Get Int Method """
        return (self.get(key, int))

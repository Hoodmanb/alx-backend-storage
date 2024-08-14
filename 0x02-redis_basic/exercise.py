#!/usr/bin/env python3
"""Initialize the Redis connection and """
import redis
import uuid
from typing import Union


class Cache:
    """Initialize the Redis connection and """

    def __init__(self):
        """Initialize the Redis connection and """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Initialize the Redis connection and """
        rand = str(uuid.uuid4())
        self._redis.set(rand, data)
        return rand

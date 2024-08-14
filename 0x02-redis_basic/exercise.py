#!/usr/bin/env python3
"""Initialize the Redis connection and """
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable[[bytes],
            Union[str, int, float, bytes]]] = None
            ) -> Union[str, int, float, bytes, None]:
        """"""
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)

            return data

    def get_str(self, key: str) -> str:
        """"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieve data as an integer."""
        return self.get(key, int)

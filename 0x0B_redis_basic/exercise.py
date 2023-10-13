#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable


class Cache():
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        if not key:
            return None

        data = self._redis.get(key)
        if data is not None and fn is not None:
            if fn is int:
                raise ValueError("Can not use 'int' callable for this key.")
            try:
                return fn(data)
            except Exception as e:
                return str(e)
        return data

    def get_str(self, key: str):
        return self.get(key, fn=lambda data: data.decode("utf-8"))

    def get_int(self, key: str):
        return self.get(key, fn=int)

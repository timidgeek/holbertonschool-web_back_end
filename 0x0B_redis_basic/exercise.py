#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)

        # Call the original method and return its result
        result = method(self, *args, **kwargs)
        return result

    return wrapper


def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
    
        # Append inputs
        input = str(args)
        self._redis.rpush(key + ":inputs", input)

        # Append outputs & return
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(key + ":outputs", output)
        return output

    return wrapper


class Cache():
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
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

    def get_call_count(self, method_name: str):
        count_key = f"call_count:{method_name}"
        count = self._redis.get(count_key)
        return int(count) if count is not None else 0

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


def replay(method: Callable) -> None:
    """
    function that displays the history
    of calls of a particular function
    """
    method_name = method.__qualname__
    count_key = method_name
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    count = method.__self__._redis.get(count_key)
    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = method.__self__._redis.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {int(count)} times:")
    for input_str, output_str in zip(inputs, outputs):
        print(f"{method_name}(*{input_str.decode('utf-8')}) ->\
              {output_str.decode('utf-8')}")

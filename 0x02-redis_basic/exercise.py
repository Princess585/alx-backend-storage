#!/usr/bin/env python3
"""Cache class in the init method"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools

def count_calls(method: Callable) -> Callable:
    """Familiarize with the INCR command"""

     @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Function tools to be used"""
        key = method.__qualname__

        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    """History call using HPUSH, LPUSH, LRANGE"""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Input and output wrapper"""

        base_key = method.__qualname__

        inputs_key = f"{base_key}:inputs"

        outputs_key = f"{base_key}:outputs"

        input_data = str(args)

        self._redis.rpush(inputs_key, input_data)

        output = method(self, *args, **kwargs)

        output_data = str(output)

        self._redis.rpush(outputs_key, output_data)

        return output

    return wrapper

def replay(method: Callable) -> None:
    """The method input and output func"""
    method_name = method.__qualname__

    input_key = "{}:inputs".format(method.__qualname__)
    output_key = "{}:outputs".format(method.__qualname__)

    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(inputs)))
    for inp, out in zip(inputs, outputs):
        print(
            "{}(*{}) -> {}".format(
                method.__qualname__, inp.decode("utf-8"), out.decode("utf-8")
            )
        )


class Cache:
    def __init__(self):
        """Returns a string"""
        self._redis = redis.Redis()
        
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that generates a random key using uuid"""
        key = str(uuid.uuid4())
        
        self._redis.set(key, data)
        
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Stores string,bytes and numbers"""
        data = self._redis.get(key)
        if data is None:
            return data

        if fn:
            collable_fn = fn(data)
        else:    
            return data

    def get_str(self, key: str) -> str:
        """Get method take a key str arg"""
        value = self._redis.get(key. fn=lambda d: d.decode("utf-8"))
        return data

    def get_int(self, key: str) -> int:
        """Two new methods: get_str and get_int"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            return None

        return value

#!/usr/bin/env python3
"""Task 3-lru_cache.py"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching system
    """
    def __init__(self):
        """
        function with cache list
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        assigns  to the dictionary `self.cache_data`
        the `item` value for the key `key`
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                remove_item = self.queue.pop(0)
                print(f"DISCARD: {remove_item}")
                del self.cache_data[remove_item]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in `self.cache_data` linked to `key`
        """
        if key and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None

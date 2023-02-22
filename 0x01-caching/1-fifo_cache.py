#!/usr/bin/env python3
"""
Fifo Caching Mechanism
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Fifo caching mechanism that inherits BaseCaching"""
    def __init__(self):
        """Initialize the fifo cache class"""
        super().__init__()

    def put(self, key, item):
        """Put an item into the cache using the key"""
        if key is not None and item is not None:
            cache = self.cache_data
            cache[key] = item
            if len(cache) > BaseCaching.MAX_ITEMS:
                key = list(cache.keys())[0]
                del self.cache_data[key]
                print(f"DISCARD: {key}")

    def get(self, key):
        """Return the value in self.cache_data li ked to key
        """
        return self.cache_data.get(key)

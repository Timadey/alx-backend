#!/usr/bin/env python3
"""
Lifo Caching Mechanism
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Lifo caching mechanism that inherits BaseCaching"""
    def __init__(self):
        """Initialize the fifo cache class"""
        super().__init__()
        self.next_discard = ""

    def put(self, key, item):
        """Put an item into the cache using the key"""
        if key is not None and item is not None:
            cache = self.cache_data
            cache[key] = item

            if len(cache) > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.next_discard]
                print(f"DISCARD: {self.next_discard}")
            self.next_discard = key

    def get(self, key):
        """Return the value in self.cache_data li ked to key
        """
        return self.cache_data.get(key)

#!/usr/bin/env python3

"""
Caching Module
"""

from basic_caching import BaseCaching


class BasicCache(BaseCaching):
    """A BaseCache class that inherits BaseCaching
    """
    def __init__(self):
        """Initialize
        """
        super().__init__()

    def put(self, key, item):
        """Put an item into the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item in cache linked to the key
        """
        item = self.cache_data.get(key)
        return item

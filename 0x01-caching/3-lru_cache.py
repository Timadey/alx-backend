#!/usr/bin/env python3

"""
Caching Module
This module contains a class BasicCache
The class contains methods that can be used to perform basic caching operations

Example:
    >> basic = BasicCache
    >> basic.put('A', 'first item')
    >> print(basic.get('A'))
    first item

    The above example initiated a new BasicCache, basic.
    Then using the put method, we added 'first item' with key 'A'
    The item added was retrieved using the get method.

Imports:
    BaseCaching: The Base method for implementing Caching operations
"""

from functools import wraps

BaseCaching = __import__("base_caching").BaseCaching


def recent_access(method):
    """Decorator that increment the access count of a key
    """
    @wraps(method)
    def wrapper(self, *args):
        if args[0] is None:
            return
        self.access_count += 1
        self.key_count[args[0]] = self.access_count
        return method(self, *args)
    return wrapper


class LRUCache(BaseCaching):
    """A LRUCache class that inherits BaseCaching
    It implements the Least Recently used caching policy

    Methods:
        put: put a new item into the cache with the given key
        get: get an item from the cache with the given key
    Inherits:
        BaseCaching
    """
    def __init__(self):
        """Initialize a new BaseCaching Class
        """
        super().__init__()
        self.access_count = 0
        self.key_count = {}

    @recent_access
    def put(self, key, item):
        """Put an item into the cache with the given key
        Args:
            key: str : The key associated with the item to be added.
                Can not be None
            item: any: The item to be added
        Return:
            Nothing
        """
        if key is None or item is None:
            return
        cache = self.cache_data
        cache[key] = item

        if len(cache) > BaseCaching.MAX_ITEMS:
            recent = self.key_count
            lru = min(recent, key=recent.get)
            del self.cache_data[lru]
            del self.key_count[lru]
            print(f"DISCARD: {lru}")

    @recent_access
    def get(self, key):
        """Get an item in cache linked to the key
        Args:
            key: str: The key that is mapped with item to be retrieved
        Return:
            item: any: the item retrieved with the key
        """
        item = self.cache_data.get(key)
        if item is None:
            del self.key_count[key]
        return item

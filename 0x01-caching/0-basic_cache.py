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


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """A BaseCache class that inherits BaseCaching
    The BasicCache contains methods for basic caching operations

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
        self.cache_data[key] = item

    def get(self, key):
        """Get an item in cache linked to the key
        Args:
            key: str: The key that is mapped with item to be retrieved
        Return:
            item: any: the item retrieved with the key
        """
        item = self.cache_data.get(key)
        return item

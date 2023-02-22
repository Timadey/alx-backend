#!/usr/bin/env python3

""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")


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

from basic_caching import BaseCaching


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
        """Initialize
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


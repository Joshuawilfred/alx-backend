#!/usr/bin/python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache Class"""
    def __init__(self):
        """Init Function"""
        super().__init__()
        self.last_key = None

    def put(self, key, item) -> None:
        """Store data using MRU"""
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item

            self.last_key = key
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_key = self.last_key
            self.cache_data.pop(discard_key)
            print(f'DISCARD: {discard_key}')

        self.last_key = key
        self.cache_data[key] = item

    def get(self, key):
        """Get data from mru"""
        value = self.cache_data.get(key)
        if value:
            self.last_key = key
        return self.cache_data.get(key, None)

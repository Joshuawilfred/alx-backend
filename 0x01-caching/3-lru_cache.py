#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class"""
    def __init__(self):
        """Init Function"""
        super().__init__()
        self.lru_keys = []

    def put(self, key, item) -> None:
        """Store the data using LRU"""
        if key is None or item is None:
            return
        if key in self.lru_keys:
            self.cache_data[key] = item

            self.lru_keys.remove(key)
            self.lru_keys.append(key)
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            self.cache_data.pop(self.lru_keys[0])
            print(f'DISCARD: {self.lru_keys[0]}')
            self.lru_keys.pop(0)

        self.lru_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get data from lru"""
        value = self.cache_data.get(key)
        if value:
            self.lru_keys.remove(key)
            self.lru_keys.append(key)

        return self.cache_data.get(key, None)

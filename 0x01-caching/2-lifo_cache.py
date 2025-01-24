#!/usr/bin/python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""
    def __init__(self):
        """Init Function"""
        super().__init__()
        self.stack = []

    def put(self, key, item) -> None:
        """Store data in LIFO"""
        if key is None or item is None:
            return

        if key in self.stack:
            self.cache_data[key] = item

            self.stack.remove(key)
            self.stack.append(key)
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_key = self.stack.pop()
            self.cache_data.pop(discard_key, None)
            print(f'DISCARD: {discard_key}')

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get data using the key"""
        return self.cache_data.get(key, None)

#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.queue = []

    def put(self, key, item) -> None:
        """store data in FIFO"""
        if key is None or item is None:
            return

        if key in self.queue:
            self.cache_data[key] = item

            self.queue.remove(key)
            self.queue.append(key)
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_ele = self.queue.pop(0)
            self.cache_data.pop(discard_ele)
            print(f'DISCARD: {discard_ele}')

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """return the value of the key"""
        return self.cache_data.get(key, None)

#!/usr/bin/python3
"""Basic dictionary"""
from typing import Any
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class"""

    def put(self, key, item):
        """Store data in a dict"""
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key) -> Any:
        """Function that returns the value in cache_data linked to key"""
        if key:
            return self.cache_data.get(key, None)
        

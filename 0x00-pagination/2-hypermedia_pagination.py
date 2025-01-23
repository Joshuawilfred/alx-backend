#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Function return a dictionary with some key-value pairs"""
        remain_idxs: List[int] = []
        idx_data: Dict[int, List] = self.indexed_dataset()
        index: int = 0 if index is None else index
        idxs_data_keys: List[int] = sorted(idx_data.keys())

        assert 0 <= index <= idxs_data_keys[-1]

        [remain_idxs.append(idx) for idx in idxs_data_keys
         if idx >= index and len(remain_idxs) <= page_size]
        data = [idx_data.get(key) for key in remain_idxs]
        next_idx = (
            remain_idxs[-1] if len(remain_idxs) - page_size == 1 else None
        )

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_idx
        }

#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for a page.

    Args:
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing start and end indexes.
    """
    return (page - 1) * page_size, page * page_size

class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset.

        Returns:
            List[List]: Cached dataset of popular baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a single page of data.

        Args:
            page (int): Current page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a page of data along with hypermedia pagination details.

        Args:
            page (int): Current page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            Dict: A dictionary containing the current page, page size, 
                  dataset, next page, previous page, and total pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
 

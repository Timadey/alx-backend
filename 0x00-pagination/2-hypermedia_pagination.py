#!/usr/bin/env python3
"""
Alx Backend Pagination

"""


import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> tuple:
    """
    Function that returns a tuple of size two containing a
    start index and an end index corresponding to the range
    of indexes to return in a list for those particular pagination
    parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from the popular baby name dataset"""
        assert (type(page) == int and type(page_size) == int)
        assert (page > 0 and page_size > 0)
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.dataset()):
            return []
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get hyper information about the database and a page"""
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        hyper = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': None if len(data) < end else page + 1,
            'prev_page': None if start < 1 else page - 1,
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
        return hyper

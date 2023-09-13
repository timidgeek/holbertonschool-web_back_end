#!/usr/bin/env python3
"""Task 1"""
import csv
import math
from typing import List


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
        pass


def index_range(page: int, page_size: int) -> tuple:
    """
    bookmark function that returns start index and an end index
    corresponding to the range of indexes for those particular
    pagination parameters
    """
    return (page_size * (page - 1), page_size * page)


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """
    function that takes two integer arguments,
    verifies they are greater than zero, uses `index_range`
    to find the correct indexes to paginate the dataset and
    return the appropriate page of the dataset
    """
    # input vaidation / verify arguments exist & are greater than zero
    assert isinstance(page, int) and isinstance(page_size, int) and \
        page > 0 and page_size > 0

    start_index, end_index = index_range(page, page_size)

    dataset = self.dataset()
    # check for out of range, if so return empty list
    if start_index >= len(dataset):
        return []

    return dataset[start_index, end_index]

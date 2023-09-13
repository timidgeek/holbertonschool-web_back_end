#!/usr/bin/env python3
"""Task 2"""
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
        """
        function that takes two integer arguments,
        verifies they are greater than zero, uses `index_range`
        to find the correct indexes to paginate the dataset and
        return the appropriate page of the dataset
        """
        # input vaidation / verify arguments exist & are greater than zero
        assert isinstance(page, int) and isinstance(page_size, int) and \
            page > 0 and page_size > 0

        (start_index, end_index) = index_range(page, page_size)
        paginationList = []  # return empty if out of range

        dataset = self.dataset()
        if end_index < len(dataset):
            for new_index in range(start_index, end_index):
                paginationList.append(dataset[new_index])

        return paginationList

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a dictionary with pagination information,
        including the following key value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        # validate input arguments
        assert isinstance(page, int) and isinstance(page_size, int) and \
            page > 0 and page_size > 0

        dataset = self.dataset()
        total_items = len(dataset)

        # ceiling value - total number of pages
        total_pages = math.ceil(total_items / page_size)
        # current page's data
        data = self.get_page(page, page_size)

        # get nxt and prev page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        pagination_info = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return pagination_info


def index_range(page: int, page_size: int) -> tuple:
    """
    bookmark function that returns start index and an end index
    corresponding to the range of indexes for those particular
    pagination parameters
    """
    return (page_size * (page - 1), page_size * page)

#!/usr/bin/env python3
"""Task 0"""


def index_range(page: int, page_size: int) -> tuple:
    """
    bookmark function that returns start index and an end index
    corresponding to the range of indexes for those particular
    pagination parameters
    """
    return (page_size * (page - 1), page_size * page)

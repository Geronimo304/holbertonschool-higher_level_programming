#!/usr/bin/env python3
"""
This module implements a counted iterator that tracks the number of
items iterated over.
"""


class CountedIterator:
    """
    A wrapper around a standard Python iterator that keeps track
    of how many items have been fetched during iteration.
    """
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        Args:
            iterable: Any iterable object (list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return self to make the CountedIterator itself iterable.
        Returns:
            self: The iterator object
        """
        return self

    def __next__(self):
        """
        Get the next item from the iterator and increment the counter.
        Returns:
            The next item from the wrapped iterator
        Raises:
            StopIteration: When there are no more items to iterate
        """
        self.count += 1

        try:
            return next(self.iterator)
        except StopIteration:
            self.count -= 1
            raise

    def get_count(self):
        """
        Get the current count of items that have been iterated.
        Returns:
            int: The number of items iterated so far
        """
        return self.count

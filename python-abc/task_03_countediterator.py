#!/usr/bin/python3
"""
This module defines the CountedIterator class, which extends the behavior
of Python iterators by keeping track of how many items have been consumed
during iteration.

It can be useful for debugging, performance analysis, or any scenario where
you need to know how many elements have been iterated over at a given point.
"""


class CountedIterator:
    """
    A class that wraps an iterable and counts how many elements have been
    retrieved via __next__.

    Methods:
        __init__(iterable): Initializes the iter and the count.
        __iter__(): Returns self to support iteration with for loops.
        __next__(): Returns the next element and increments the count.
        get_count(): Returns the number of iterated elements.
    """

    def __init__(self, iterable):
        self.iter = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iter)
        self.count += 1
        return item

    def get_count(self):
        return self.count

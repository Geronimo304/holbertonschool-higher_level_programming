#!/usr/bin/env python3
"""
This module implements a verbose version of the Python list class
that prints notification messages when items are added or removed.
"""


class VerboseList(list):
    """
    A custom list class that prints notification messages when items
    are added or removed.
    Inherits from the built-in list class and extends its functionality.
    """
    def append(self, item):
        """
        Add an item to the list and print a notification.
        Args:
            item: The item to add to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a notification.
        Args:
            iterable: The iterable containing items to add to the list
        """
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification.
        Args:
            item: The item to remove from the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item at the given index and print a notification.
        Args:
            index (int, optional): The index of the item to remove.
            Defaults to -1 (last item).
        Returns:
            The item that was removed
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

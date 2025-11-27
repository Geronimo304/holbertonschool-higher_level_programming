#!/usr/bin/python3
"""Module that defines a class with restricted instance attributes."""


class LockedClass():
    """Class that prevents dynamic attribute creation, except 'first_name'.

    The use of __slots__ restricts the instance to only allow the 'first_name'
    attribute, saving memory and avoiding the creation of other attributes.
    """
    __slots__ = ('first_name',)

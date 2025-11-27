#!/usr/bin/python3
"""
Module containing the say_my_name function.

This function prints the full name given a first name and last name,
validating that both are strings.

Raises exceptions if the arguments do not pass the validations.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format: "My name is <first_name> <last_name>".
    """

    if not first_name or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name:s} {last_name:s}")

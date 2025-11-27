#!/usr/bin/python3
"""
text_indentation module.

This module provides a single function, `text_indentation`,
which prints a given text with two new lines after each of
the following punctuation marks: '.', '?', and ':'.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input string to format.

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] not in (".", "?", ":"):
            print(text[i], end="")
            i += 1
        else:
            print(f"{text[i]:s}\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1

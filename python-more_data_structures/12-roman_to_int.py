#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_libr = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total_char = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_libr.get(char, 0)
        if value < prev_value:
            total_char -= value
        else:
            total_char += value
            prev_value = value
    return total_char

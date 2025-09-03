#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        print(f"{number % 10}", end="")
        return number % 10
    elif number == 0:
        print(f"{number}", end="")
        return number
    elif number < 0:
        print(f"{-number % 10}", end="")
        return -number % 10
    else:
        print(number)
        return number

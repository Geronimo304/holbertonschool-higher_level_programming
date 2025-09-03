#!/usr/bin/python3
def print_last_digit(number):
        if number > 0:
            print(f"{number % 10}")
        elif number == 0:
             print(number)
        else:
            neg = number * -1
            print(f"-{number % 10}")        

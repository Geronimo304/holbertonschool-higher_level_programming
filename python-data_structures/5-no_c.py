#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new_list += letter
    return new_list

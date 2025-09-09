#!/usr/bin/python3
def no_c(my_string):
    guradar_caracter = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            guradar_caracter += i
    return guradar_caracter

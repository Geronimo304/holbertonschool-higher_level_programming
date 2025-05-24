#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    gero = []
    for number in my_list:
        gero.append(number % 2 == 0)
    return gero

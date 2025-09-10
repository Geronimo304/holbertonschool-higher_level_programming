#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    elif all(isinstance(x, int) for x in my_list):
        maximo = my_list[0]
        for i in my_list:
            if i > maximo:
                maximo = i
        return maximo
    else:
        return None

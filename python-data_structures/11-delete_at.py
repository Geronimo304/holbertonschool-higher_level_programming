#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    result = []
    if idx > 0:
        my_list.remove(my_list[idx])
        return my_list
    else:
        return my_list

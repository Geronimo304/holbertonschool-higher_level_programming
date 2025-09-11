#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lista_nueva = []
    for i in my_list:
        if i == search:
            lista_nueva.append(replace)
        else:
            lista_nueva.append(i)
    return lista_nueva


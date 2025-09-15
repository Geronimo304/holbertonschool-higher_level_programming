#!/usr/bin/python3
def uniq_add(my_list=[]):
    resultado = 0
    lista = []
    for i in my_list:
        if i not in lista:
            resultado += i
            lista.append(i)
    return resultado
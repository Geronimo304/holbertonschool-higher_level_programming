#!/usr/bin/python3
""" Declaramos la funcion. """


class MyList(list): 
   """Creamos la class mylist heredada de list"""
   def print_sorted(self):
        """Declaramos la funcion"""
        lista = sorted(self)
        print(lista)

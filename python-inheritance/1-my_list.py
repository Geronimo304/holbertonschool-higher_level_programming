#!/usr/bin/python3
""" Declaramos la funcion. """



class MyList(list): 
   def print_sorted(self):
        """Creamos la class mylist heredada de list"""
        lista = sorted(self)
        print(lista)

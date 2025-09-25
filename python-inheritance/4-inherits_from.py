#!/usr/bin/python3
""" Defino una funcion. """


def inherits_from(obj, a_class):
    """ Con isinstance me fijo si son objetos heredados de la clase"""
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""inicializo la class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """uso init para crear los objetos"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Devuelve los atributos como instancias"""
        return self.__dict__

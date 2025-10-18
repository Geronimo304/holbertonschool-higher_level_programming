#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """inizialiso student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retorno el diccionario"""
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

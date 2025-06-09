#!/usr/bin/python3
"""recupera nombres de atributos"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                result = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        result[attr] = getattr(self, attr)
                return result
        return self.__dict__

    def reload_from_json(self, json):
        """recarga los atributos del objeto student"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)

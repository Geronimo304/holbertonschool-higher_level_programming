#!/usr/bin/python3
"""
This module defines an abstract base class `Animal` and its subclasses `Cat` and `Dog`.

The `Animal` class enforces the implementation of the `sound()` method in all subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    Subclasses must implement the `sound()` method to define
    the sound the animal makes.
    """

    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    """
    A subclass of Animal that represents a cat.
    """

    def sound(self):
        return "Meow"


class Dog(Animal):
    """
    A subclass of Animal that represents a dog.
    """

    def sound(self):
        return "Bark"

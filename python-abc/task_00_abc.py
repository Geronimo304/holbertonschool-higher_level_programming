#!/usr/bin/python3
"""
This module implements an example of abstract classes in Python using the ABC module.
It demonstrates how to create an abstract base class and concrete subclasses that implement it.
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract class that defines the base structure for all animals.
    This class cannot be instantiated directly. It serves as a template
    to ensure that all subclasses implement the required methods.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses.
        Returns:
            str: The sound made by the animal
        Note: This method has no implementation in the base class.
        """
        pass


class Dog(Animal):
    """
    Class representing a dog.
    Inherits from the Animal abstract class and implements the sound() method.
    """
    def sound(self):
        """
        Implements the abstract sound() method for the Dog class.
        Returns:
            str: The characteristic sound of a dog ("Bark")
        """
        return "Bark"

class Cat(Animal):
    """
    Class representing a cat.
    Inherits from the Animal abstract class and implements the sound() method.
    """
    def sound(self):
        """
        Implements the abstract sound() method for the Cat class.
        Returns:
            str: The characteristic sound of a cat ("Meow")
        """
        return "Meow"
    
#!/usr/bin/python3
"""
This module demonstrates multiple inheritance in Python by defining
two parent classes, Fish and Bird, and a subclass FlyingFish that inherits
from both. It showcases method overriding and the concept of method
resolution order (MRO).
"""


class Fish:
    """
    Represents a fish with swimming abilities and a water habitat.

    Methods:
        swim(): Prints a message indicating the fish is swimming.
        habitat(): Prints the natural habitat of the fish.
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with flying abilities and a sky habitat.

    Methods:
        fly(): Prints a message indicating the bird is flying.
        habitat(): Prints the natural habitat of the bird.
    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish that inherits behaviors from both Fish and Bird.

    This class overrides:
        fly(): To indicate the flying fish is soaring.
        swim(): To indicate the flying fish is swimming.
        habitat(): To indicate the flying fish lives both in water and the sky

    Inherits:
        Fish, Bird
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

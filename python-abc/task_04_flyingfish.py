#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance in Python through
implementation of a FlyingFish class that inherits from both
Fish and Bird parent classes.
"""


class Fish:
    """
    A class representing basic fish behavior and characteristics.
    Provides methods for swimming and defining aquatic habitat.
    """
    def swim(self):
        """
        Simulate the swimming behavior of a fish.
        Prints a message indicating the fish is swimming.
        """
        print(f"The fish is swimming")

    def habitat(self):
        """
        Describe the natural habitat of a fish.
        Prints a message indicating fish live in water.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing basic bird behavior and characteristics.
    Provides methods for flying and defining aerial habitat.
    """
    def fly(sel):
        """
        Simulate the flying behavior of a bird.
        Prints a message indicating the bird is flying.
        """
        print("The birds is flying")

    def habitat(self):
        """
        Describe the natural habitat of a bird.
        Prints a message indicating birds live in the sky.
        """
        print("The birds lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish that inherits from both Fish and Bird.
    Demonstrates multiple inheritance by combining and overriding methods
    from both parent classes.

    Note on Method Resolution Order (MRO):
    Methods are resolved first in FlyingFish, then Fish, then Bird,
    and finally object.
    This order is determined by the sequence of parent classes in the classe
    definition.
    """
    def fly(self):
        """
        Override the flying behavior for a flying fish.
        Prints a message indicating the flying fish's unique
        soaring behavior.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override the swimming behavior for a flying fish.
        Prints a message indicating the flying fish's swimming behavior.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override the habitat description for a flying fish.
        Prints a message indicating the flying fish's dual habitat in both
        water and sky.
        """
        print("The flying fish lives both in water and the sky!")

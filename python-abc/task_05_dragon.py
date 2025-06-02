#!/usr/bin/env python3
"""
This module demonstrates the use of mixins in Python to compose behaviors
in classes without deep inheritance hierarchies. It implements swimming and
flying capabilities as mixins and combines them in a Dragon class.
"""


class SwimMixin:
    """
    A mixin that provides swimming capability to any class that inherits
    from it.
    This is an example of composition through inheritance.
    """
    def swim(self):
        """
        Simulate swimming behavior.
        Prints a message indicating the creature is swimming.
        """
        print(f"The creature swims!")


class FlyMixin:
    """
    A mixin that provides flying capability to any class that inherits
    from it.
    This is an example of composition through inheritance.
    """
    def fly(self):
        """
        Simulate flying behavior.
        Prints a message indicating the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon that can both swim and fly.
    Demonstrates how mixins can be used to compose behaviors
    from multiple sources.

    The Dragon class inherits swimming ability from SwimMixin
    and flying ability from FlyMixin, showing how mixins can be
    combined to create classes with multiple capabilities.
    """
    def roar(self):
        """
        Simulate the roaring behavior specific to dragons.
        Prints a message indicating the dragon is roaring.
        """
        print(f"The dragon roars!")

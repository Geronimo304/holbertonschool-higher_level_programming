#!/usr/bin/python3


class SwimMixin:
    """
    Mixin class that provides swimming capability.
    This class is designed to be combined with other classes
    to add swimming behavior without standalone functionality.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability.
    This class is designed to be combined with other classes
    to add flying behavior without standalone functionality.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Represents a Dragon that can both swim and fly by inheriting
    behaviors from SwimMixin and FlyMixin.

    Additional methods specific to Dragon can be added here.
    """

    def roar(self):
        print("The dragon roars!")

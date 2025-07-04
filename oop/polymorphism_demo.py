# A python script whose objective is to enhance understanding of polymorphism through set of classes that demonstrate method overriding and polymorphic behaviour.

import math

class Shape:
    """Base class for all shapes."""

    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must override this method.")

class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""

    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle. overrides the area method from base class."""
        return self.length * self.width

class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
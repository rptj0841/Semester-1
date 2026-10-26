# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    # Add distance() method here
    def distance(self):
        """
        Returns distance from this Point to origin.
        """
        return math.hypot(self.x, self.y)

    # Add distance_to() method here

    def distance_to(self, point2):
        """
        Returns distance from this point to another point given.
        """
        return abs(math.hypot(point2.x, point2.y) - math.hypot(self.x, self.y))

# Add a definition for a Circle class here, giving it
class Circle:
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)

    def __init__(self, radius, centre):
        self.radius = radius
        self.centre = centre

#  - A method area(), returning the area of the circle

    def area(self):
        return math.pi * self.radius**2

#  - A method perimeter(), returning the perimeter of the circle
    def perimeter(self):
        return math.pi * 2 * self.radius

# Don't add any testing code to this file!


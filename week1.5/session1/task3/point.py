# Week 1.5, Session 1: Task 3

import math

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



# Finally, add code here to demonstrate use of Point#

p1 = Point(3,4)
p2 = Point(6,7)
print(p1.distance())
print(p2.distance())
print(p1.distance_to(p2))
print(p2.distance_to(p1))

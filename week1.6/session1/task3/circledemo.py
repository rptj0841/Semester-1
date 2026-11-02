# Week 1.6, Session 1: Task 3

import math
from point import Point
from shapes import Shape, Circle

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

point = Point(0,0)
circle = Circle(point, "red", 2.5)
print(circle.__str__())
print(circle.area())
print(circle.perimeter())
newPos = Point(1.6,3.2)
circle.set_position(newPos)
print(circle.__str__())
circle.set_colour("green")
print(circle.__str__())
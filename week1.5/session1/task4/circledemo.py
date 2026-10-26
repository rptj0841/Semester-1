# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
import math
import geometry
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
circleCentre = geometry.Point(3,4)
#  - Creates a Circle object, using the Point object and a value for radius
circle = geometry.Circle(5, circleCentre)
#  - Displays the area of the circle
print(circle.area())
#  - Displays the perimeter of the circle
print(circle.perimeter())
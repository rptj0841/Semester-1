# A bad class implementation

# What does the runtime error mean?
# TypeError: Pint.__init__() takes 2 positional arguments but 3 were given.

# How do we fix the code?
# Add self in the parameter list and self. before each attribute defintion

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)


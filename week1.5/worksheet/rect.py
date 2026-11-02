# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Width and height must be integers")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0")

        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

    def is_square(self):
        """
        Checks whether the rectangle is a square by checking the width and height.
        """
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """
        Calculates and returns the value of the area of the rectangle
        """
        return self.width*self.height

    def perimeter(self):
        """
        Calculates and returns the value of the perimeter of the rectangle.
        """
        return (self.width+self.height) * 2

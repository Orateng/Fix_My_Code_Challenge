#!/usr/bin/python3

class square():
   """Class representing a square."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Instantiation of class attributes."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.width

    def perimiter_of_my_square(self):
        """Calculates perimeter of the sqaure."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns a string representation."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

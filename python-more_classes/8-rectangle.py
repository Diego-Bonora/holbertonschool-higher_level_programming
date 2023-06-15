#!/usr/bin/python3
"""
Rectangle class with private instance attrivutes and the getters and setters
Function for returning area and perimeter of the rectangle
__str__ prints the rectangle
__repr__ prints the representation of the
__del__ shows a message when deleted
counter for the amount of instances are created
"""


class Rectangle:
    """ rectangle class with width and height attrivutes """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0) -> None:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self) -> str:
        new_str = ""
        if self.__height == 0 or self.__width == 0:
            return new_str
        else:
            for height in range(self.__height):
                for widht in range(self.__width):
                    new_str += str(self.print_symbol)
                if height < self.__height - 1:
                    new_str += "\n"
            return new_str

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        del self
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            area_1 = rect_1.area()
            area_2 = rect_2.area()
            if area_1 >= area_2:
                return rect_1
            else:
                return rect_2

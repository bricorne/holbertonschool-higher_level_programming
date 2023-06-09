#!/usr/bin/python3
"""define square"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """area size"""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end='')
                print()

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position"""
        if (type(value) is not tuple or len(value) != 2
           or type(value[0]) is not int or type(value[1]) is not int
           or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

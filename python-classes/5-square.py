#!/usr/bin/python3
"""define square"""


class Square:
    """Square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
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

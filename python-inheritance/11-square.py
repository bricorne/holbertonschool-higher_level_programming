#!/usr/bin/python3
"""define class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inirite Rectangle"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """return area"""
        return self.__size ** 2

    def __str__(self):
        """def string"""
        return f"[Square] {self.__size}/{self.__size}"
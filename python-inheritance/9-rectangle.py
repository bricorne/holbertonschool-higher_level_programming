#!/usr/bin/python3
"""define class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inirite BaseGeometry"""
    def __init__(self, width, height):
        """define size"""
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
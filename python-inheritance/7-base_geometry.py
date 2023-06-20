#!/usr/bin/python3
"""define class BaseGeometry"""


class BaseGeometry:
    """class"""
    def area(self):
        """define area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """def int validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
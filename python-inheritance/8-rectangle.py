#!/usr/bin/python3
"""define class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inirite BaseGeometry"""
    def __init__(self, width, height):
        """define size"""
        self.width = width
        self.height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)
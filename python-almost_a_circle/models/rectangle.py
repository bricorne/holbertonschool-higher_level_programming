#!/usr/bin/python3
"""create class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width """
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @property
    def x(self):
        """ x """
        return self.__x

    @property
    def y(self):
        """ y """
        return self.__y

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height
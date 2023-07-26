#!/usr/bin/python3
"""returns True if the object is an instance"""


def inherits_from(obj, a_class):
    """function"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
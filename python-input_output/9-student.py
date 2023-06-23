#!/usr/bin/python3
"""class Student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary"""
        json_dict = {}
        for attr, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[attr] = value
        return json_dict
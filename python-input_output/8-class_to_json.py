#!/usr/bin/python3
"""returns the dictionary"""


def class_to_json(obj):
    """returns the dictionary"""
    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
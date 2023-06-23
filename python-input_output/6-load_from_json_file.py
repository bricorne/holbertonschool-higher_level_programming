#!/usr/bin/python3
"""creates an Object"""


import json

def load_from_json_file(filename):
    """creates an Object"""
    with open(filename, "r") as file:
        my_obj = json.load(file)
    return my_obj
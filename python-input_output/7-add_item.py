#!/usr/bin/python3
"""adds all arguments"""


import sys
_save = __import__('5-save_to_json_file').save_to_json_file
_load = __import__('6-load_from_json_file').load_from_json_file

def add_arguments_to_list(arguments):
    """adds all arguments"""
    try:
         my_list = _load("add_item.json")
    except FileNotFoundError:
         my_list = []
    
    my_list.extend(arguments)
    _save(my_list, "add_item.json")

arguments = sys.argv[1:]

add_arguments_to_list(arguments)
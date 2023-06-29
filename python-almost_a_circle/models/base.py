#!/usr/bin/python3
"""create class Base"""
import json

class Base:
    """class base"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
        
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string"""
        if list_objs is None:
            list_objs = []
        
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        
        with open(filename, 'w') as file:
            file.write(json_string)
    
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        
        obj_list = cls.from_json_string(json_string)
        return [cls.create(**obj_dict) for obj_dict in obj_list]
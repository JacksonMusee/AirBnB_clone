#!/usr/bin/python3
"""
In this model we have a class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
<class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> ->
<class 'BaseModel'>
"""

import json
import os
import copy


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Retrieve all objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Add object obj to __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        my_objects = copy.deepcopy(self.__objects)

        for key, value in my_objects.items():
            my_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as j_file:
            json.dump(my_objects, j_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        """
        from models.base_model import BaseModel

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as j_file:
                self.__objects = json.load(j_file)

        for key, value in self.__objects.items():
            self.__objects[key] = BaseModel(**value)

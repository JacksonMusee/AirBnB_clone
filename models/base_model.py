#!/usr/bin/python3
"""
This' where the main class of our website's objects will be defined.
The BaseModel its methods
"""

import datetime
import json
import uuid


class BaseModel:
    """
    Defines all common attributes/methods for other classes of the AirBnB
    clone website
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.datetime.fromisoformat(value)

                if key == 'updated_at':
                    value = datetime.datetime.fromisoformat(value)

                if key != '__class__':
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Out put string when an instance of BaseModel is printed
        """
        string = (
                f"[{self.__class__.__name__}] "
                f"({self.id}) "
                f"{self.__dict__}"
                )
        return (string)

    def save(self):
        """
        Updated updated_at with current time
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance with
        __class__ added
        """
        the_dct = self.__dict__.copy()
        the_dct['__class__'] = self.__class__.__name__
        the_dct['created_at'] = self.created_at.isoformat()
        the_dct['updated_at'] = self.updated_at.isoformat()
        return (the_dct)

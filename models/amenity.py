#!/usr/bin/python3
"""
Every living space has amenities.
They are defined here
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Blueprint of creating an amenity
    """
    name = ""

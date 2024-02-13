#!/usr/bin/python3
"""
All  great cities live here
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    A blueprint for building a city
    """
    state_id = ""
    name = ""

#!/usr/bin/python3
"""
Ofcourse use have alot to say about AirBnB
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    A review is simple. Blueprint here
    """
    place_id = ""
    user_id = ""
    text = ""

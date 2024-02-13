#!/usr/bin/python3
"""
Write a class User that inherits from BaseModel:
models/user.py
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the type of all users
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

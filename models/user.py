#!/usr/bin/python3
"""
Write a class User that inherits from BaseModel:
models/user.py
"""

from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """
    This is the type of all users
    """
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

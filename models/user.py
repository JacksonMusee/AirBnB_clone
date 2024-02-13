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
    self.email = ""
    self.password = ""
    self.first_name = ""
    last_name = ""

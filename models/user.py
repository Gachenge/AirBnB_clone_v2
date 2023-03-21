#!/usr/bin/python3
"""define the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ define the user class that inherits from base model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

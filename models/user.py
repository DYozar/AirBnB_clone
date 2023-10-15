#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the User class."""
=======
"""This module creates a User class"""
>>>>>>> 82ecdfe5c2966aa050f5412b630fe2b15ffa7c87
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
=======
    """Class for managing user objects"""
>>>>>>> 82ecdfe5c2966aa050f5412b630fe2b15ffa7c87

    email = ""
    password = ""
    first_name = ""
    last_name = ""

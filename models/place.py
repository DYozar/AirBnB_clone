#!/usr/bin/python3
<<<<<<< HEAD
"""Contains the Place model"""
=======
"""This module creates a Place class"""

>>>>>>> 82ecdfe5c2966aa050f5412b630fe2b15ffa7c87
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """
    Implements the Place model

    Args:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """
=======
    """Class for managing place objects"""

>>>>>>> 82ecdfe5c2966aa050f5412b630fe2b15ffa7c87
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
<<<<<<< HEAD
    amenity_ids = []
=======
    amenity_ids = []
>>>>>>> 82ecdfe5c2966aa050f5412b630fe2b15ffa7c87

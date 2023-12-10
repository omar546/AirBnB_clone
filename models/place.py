#!/usr/bin/python3
"""
module defines the Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class represents information about the place for rent.
    Attributes:
    - city_id (str): ID of the city.
    - user_id (str): ID of the user.
    - name (str): name of the place.
    - description (str): description of the place.
    - longitude (float): longitude coordinate.
    - amenity_ids (list): list of amenity IDs.
    - number_rooms (int): number of rooms.
    - number_bathrooms (int): number of bathrooms in the place.
    - max_guest (int): maximum number of guests.
    - price_by_night (int): The price per night.
    - latitude (float): The latitude coordinate.
    """
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    city_id = ""
    user_id = ""
    max_guest = 0
    price_by_night = 0


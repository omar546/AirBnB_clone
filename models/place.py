#!/usr/bin/python3
"""
module defines the Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class represents information about the place for rent.
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


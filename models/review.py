#!/usr/bin/python3
"""
module defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    used to create and manage review objects.

    Attributes:
        place_id (str): ID of the place.
        user_id (str): ID of the user.
        text (str): content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""

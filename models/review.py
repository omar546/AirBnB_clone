#!/usr/bin/python3
"""
module defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    used to create and manage review objects.
    """
    place_id = ""
    user_id = ""
    text = ""

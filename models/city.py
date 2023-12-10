#!/usr/bin/python3
"""
module defines the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    city inherits from the BaseModel
    class.
    """
    state_id = ""
    name = ""

#!/usr/bin/python3
"""
module defines the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class Amenity inherits BaseModel.

    Attributes:
    - name (str): The name of the Amenity.
    """
    name = ""

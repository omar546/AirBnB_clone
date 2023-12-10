#!/usr/bin/python3
"""
module defines the State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    subclass of BaseModel

    Attributes:
        name (str): The name of the state.
    """
    name = ""

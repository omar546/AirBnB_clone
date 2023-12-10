#!/usr/bin/python3
"""BaseModel class to define a foundation for other classes"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """
    The foundation class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"] :
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        class_name = self.__class__.__name__
        formatted_created_at = self.created_at.isoformat()
        formatted_updated_at = self.updated_at.isoformat()

        obj_dict = {
            "__class__": class_name,
            "created_at": formatted_created_at,
            "updated_at": formatted_updated_at
        }

        for key, value in self.__dict__.items():
            if key not in obj_dict:
                obj_dict[key] = value

        return obj_dict


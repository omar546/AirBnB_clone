#!/usr/bin/python3

"""FileStorage class Module"""

from models.base_model import BaseModel
import datetime
import os
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add new object"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save to JSON"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fi:
            di = {ky: val.to_dict() for ky, val in FileStorage.__objects.items()}
            json.dump(di, fi)

    def reload(self):
        """reload from JSON"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    # def classes(self):
    #     from models.base_model import BaseModel
    #     from models.user import User
    #     from models.state import State
    #     from models.city import City
    #     from models.amenity import Amenity
    #     from models.place import Place
    #     from models.review import Review

    #     classes = {"BaseModel": BaseModel,
    #                "User": User,
    #                "State": State,
    #                "City": City,
    #                "Amenity": Amenity,
    #                "Place": Place,
    #                "Review": Review}
    #     return classes
    
    # def attributes(self):
    #     attributes = {
    #         "BaseModel":
    #                  {"id": str,
    #                   "created_at": datetime.datetime,
    #                   "updated_at": datetime.datetime},
    #         "User":
    #                  {"first_name": str,
    #                   "last_name": str,
    #                   "email": str,
    #                   "password": str
    #                   },
    #         "State":
    #                  {"name": str},
    #         "City":
    #                  {"state_id": str,
    #                   "name": str},
    #         "Amenity":
    #                  {"name": str},
    #         "Place":
    #                  {"city_id": str,
    #                   "user_id": str,
    #                   "name": str,
    #                   "description": str,
    #                   "price_by_night": int,
    #                   "latitude": float,
    #                   "longitude": float,
    #                   "number_rooms": int,
    #                   "number_bathrooms": int,
    #                   "max_guest": int,
    #                   "amenity_ids": list},
    #         "Review":
    #         {"place_id": str,
    #             "user_id": str,
    #             "text": str}
    #     }
    #     return attributes
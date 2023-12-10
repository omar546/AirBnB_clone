#!/usr/bin/python3

"""FileStorage class Module"""
import json


class FileStorage:
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        return self.__objects

    def new(self, obj):
        """add new object"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        """reload from JSON"""
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review, }
        serialized_objects = {}
        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, val in serialized_objects.items():
                    self.__objects[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

from models import storage
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        pass

"""BaseModel class to define a foundation for other classes"""
import uuid
from datetime import datetime
from cmd import Cmd


class BaseModel(Cmd):
    """
    The foundation class.

    Attributes:
        - id (str): unique identifier for each instance.
        - created_at (datetime): timestamp at creation.
        - updated_at (datetime): timestamp update.

    Methods:
        - __init__: Initializes a new instance of the class.
        - __str__: a string representation.
        - save: saves the instance to storage & Updates the 'updated_at'.
        - to_dict: Converts the instance to a dictionary for serialization.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

        Args:
            - *args: arguments -not used.
            - **kwargs: keyword arguments for deserialization.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"] :
                    '''Convert created_at and updated_at strings to datetime objects'''
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

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

        obj_dict.update(self.__dict__)
        return obj_dict

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


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    # print(type(my_model.created_at))
    # print("--")
    # my_model_json = my_model.to_dict()
    # print(my_model_json)
    # print("JSON of my_model:")
    # for key in my_model_json.keys():
    #     print("\t{}: ({}) - {}".format(key,
    #           type(my_model_json[key]), my_model_json[key]))

    # print("--")
    # my_new_model = BaseModel(**my_model_json)
    # print(my_new_model.id)
    # print(my_new_model)
    # print(type(my_new_model.created_at))

    # print("--")
    # print(my_model is my_new_model)

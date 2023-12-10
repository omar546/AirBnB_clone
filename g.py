my_function = "5*x**2 + 8*x - 2"


def f(x):
    return eval(my_function)


print(f(0))

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
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))

                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

eval("BaseModel")
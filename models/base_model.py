#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    """BaseModel class for creating and managing instances."""
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, self.TIME_FORMAT)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def __str__(self) -> str:
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save the instance."""
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self) -> dict:
        """Return a dictionary of instance attributes."""
        excluded = ['name', 'my_number']
        result = {i: y for i, y in self.__dict__.items() if i not in excluded}
        result['__class__'] = self.__class__.__name__

        for i, y in result.items():
            if isinstance(y, datetime):
                result[i] = y.isoformat()

        return result


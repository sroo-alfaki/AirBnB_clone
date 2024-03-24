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

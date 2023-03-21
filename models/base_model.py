#!/usr/bin/python3
"""define the base model for all other classes"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """this class will define all other objects and attributes"""

    def __init__(self, *args, **kwargs):
        """initialise all attributes to be used
        id: should be unique every time and generated using uuid4
        created_at: first call of this should be have a time stamp
        updated_at: renewable time stamp
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return the string representation"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__.copy())

    def save(self):
        """updates the updated_at time stamp"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary containing key value pairs"""
        myDict = self.__dict__.copy()
        myDict["__class__"] = str(type(self).__name__)
        myDict["created_at"] = self.created_at.isoformat()
        myDict["updated_at"] = self.updated_at.isoformat()
        return myDict

#!/usr/bin/python3
"""define the base model for all other classes"""
from sqlalchemy.ext.declarative import declarative_base
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

Base = declarative_base()


class BaseModel:
    """this class will define all other objects and attributes
    id - the model id
    created_at - time the model was created
    updated_at - last time edited
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """initialise all attributes to be used
        id: should be unique every time and generated using uuid4
        created_at: first call of this should be have a time stamp
        updated_at: renewable time stamp
        """

        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """updates the updated_at time stamp"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """dictionary containing key value pairs"""
        myDict = self.__dict__.copy()
        myDict["__class__"] = str(type(self).__name__)
        myDict["created_at"] = self.created_at.isoformat()
        myDict["updated_at"] = self.updated_at.isoformat()
        myDict.pop("_sa_instance_state", None)
        return myDict

    def delete(self):
        """ delete object
        """
        models.storage.delete(self)

    def __str__(self):
        """string representation of the basemodel"""
        bm = self.__dict__.copy()
        bm.pop("_sa_instance_state", None)
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, bm))

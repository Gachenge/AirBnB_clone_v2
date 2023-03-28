#!/usr/bin/python3
"""class state also inherits from BaseModel"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column
import models
from models.city import City
from models.base_model import Base
from sqlalchemy import String
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete",
                          backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """list of all related objects"""
            cityls = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cityls.append(city)
            return cityls

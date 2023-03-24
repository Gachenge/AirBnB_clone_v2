#!/usr/bin/python3
"""class city that inherits from BaseModel"""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import String


class City(BaseModel, Base):
    """has attributes state id and name
    city inherits from Basemodel
    has attributes:
        name: maximum 128 characters, not nullable
        state_id: maximum 60 characters and serves as the foreign key
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

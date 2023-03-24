#!/usr/bin/python3
from models.base_model import BaseModel, Base
"""class city that inherits from BaseModel"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

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
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")

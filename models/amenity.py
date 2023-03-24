#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity
"""amenity class inherits from Basemodel"""


class Amenity(BaseModel):
    """has just a name attribute
    name has a maximum 128 characters
    the column is not nullable
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)

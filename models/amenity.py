#!/usr/bin/python3
"""Defines the amenity class"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from models.base_model import Base
from sqlalchemy import String


class Amenity(BaseModel, Base):
    """has just a name attribute
    name has a maximum 128 characters
    the column is not nullable
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)

#!/usr/bin/python3
"""define the user class"""
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from models.base_model import Base


class User(BaseModel, Base):
    """ define the user class that inherits from base model
    email: max 128 chars not null
    password: max 128 chars not null
    first_name: max 128 chars
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

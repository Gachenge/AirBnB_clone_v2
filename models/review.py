#!/usr/bin/python3
"""review class inherits from basemodel"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel):
    """has attributes place_id, user_id and text
    text: max 1024 chars, not null
    place_id: max 60 chars, foreign key
    user_id: max 60 chars, foreign key
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

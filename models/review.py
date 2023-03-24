#!/usr/bin/python3
"""review class inherits from basemodel"""
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


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

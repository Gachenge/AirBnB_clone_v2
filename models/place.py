#!/usr/bin/python3
"""class place inherits from basemodel"""
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table


association = Table("place_amenity", Base.metadata,
                     Column("place_id", String(60),
                            ForeignKey("places.id"),
                            primary_key=True,
                            nullable=False),
                     Column("amenity_id", String(60),
                            ForeignKey("amenities.id"),
                            primary_key=True,
                            nullable=False))


class Place(BaseModel, Base):
    """has more public class attributes
    city_id: max 60 chars, foreign key
    user_id: max 128 chars, foreign key
    name: max 128 chars, not null
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """linked reviews"""
            reviewls = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviewls.append(review)
            return reviewls

        @property
        def amenities(self):
            """get the amenities"""
            amenityls = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenityls.append(amenity)
            return amenityls

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

#!/usr/bin/python3
from models.base_model import BaseModel

"""review class inherits from basemodel"""


class Review(BaseModel):
    """has attributes place_id, user_id and text"""

    place_id = ""
    user_id = ""
    text = ""

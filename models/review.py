#!usr/bin/python3
"""
    Class Review that inherits from BaseModel,
    and contains all data about review class.
"""
from models import BaseModel


class Review(BaseModel):
    """
    Represents all the attributes.
    """
    place_id = ""
    user_id = ""
    text = ""

#!usr/bin/python3
"""
    Class Review that inherits from BaseModel,
    and contains all data about review class.
"""
from .base_model import BaseModel
from models import User, Place
import .models


class place(BaseModel):
    """
    Represents all the attributes.
    """
    place_id = Place.id()
    user_id = User.id()
    text = ""

#!usr/bin/python3
"""
    Class Review that inherits from BaseModel,
    and contains all data about review class.
"""
import models


class Review(models.BaseModel):
    """
    Represents all the attributes.
    """
    place_id = ""
    user_id = ""
    text = ""

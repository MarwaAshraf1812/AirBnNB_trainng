#!usr/bin/python3
"""
    Class User that inherits from BaseModel,
    and contains all data about user class
"""
import models


class User(models.BaseModel):
    """
    Represents all the attributes.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

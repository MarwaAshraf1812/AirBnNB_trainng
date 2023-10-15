#!usr/bin/python3
"""
    Class City that inherits from BaseModel,
    and contains all data about city class.
"""
from models import BaseModel, state


class City(BaseModel):
    """
    Represents all the attributes.
    """
    state_id = state.id()
    name = ""

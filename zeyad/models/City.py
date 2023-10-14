#!usr/bin/python3
"""
    Class City that inherits from BaseModel,
    and contains all data about city class.
"""
from .base_model import BaseModel
from models import state


class city(BaseModel):
    """
    Represents all the attributes.
    """
    state_id = state.id()
    name = ""

#!usr/bin/python3
"""
    Class City that inherits from BaseModel,
    and contains all data about city class.
"""
import models


class City(models.BaseModel):
    """
    Represents all the attributes.
    """
    state_id = models.state.id()
    name = ""

#!usr/bin/python3
"""
    Class Place that inherits from BaseModel,
    and contains all data about place class.
"""
import models


class Place(models.BaseModel):
    """
    Represents all the attributes.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

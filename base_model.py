#!/usr/bin/python3
"""
defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime
from __init__ import storage
import models


class BaseModel():
    """
    Represents the BaseModel of the AirBnB project.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        standard = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == 'created_at' or 'updated_at':
                    setattr(self, key, datetime.strptime(value, standard) )
                else :
                    setattr(self, key, value)
        else :
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.
        """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Update updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """
        returns a dictionary containing all 
        keys/values of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = str(dict["created_at"].isoformat())
        dict["updated_at"] = str(dict["updated_at"].isoformat())
        return dict

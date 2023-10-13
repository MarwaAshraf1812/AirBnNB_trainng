#!/usr/bin/python3
from uuid import uuid4, isoformat
from datetime import datetime

class BaseModel():

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__.copy()

        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = str(dict["created_at"].isoformat())
        dict["updated_at"] = str(dict["updated_at"].isoformat())

        # for key, value in dict.items():
        #     if isinstance(value, datetime):
        #         dict[key] = value.isoformat()

        return dict
    
    
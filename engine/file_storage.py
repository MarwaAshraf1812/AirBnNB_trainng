#!/usr/bin/python3
import json
from datetime import datetime
class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        
        data_to_save = {key: value.__dict__ for key, value in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data_to_save, file)

    def reload(self):
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    self.__objects = json.load(file)
            except FileNotFoundError:
                pass
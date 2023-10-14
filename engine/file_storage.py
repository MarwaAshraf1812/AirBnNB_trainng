#!/usr/bin/python3
"""
Defines the FileStorage class.
"""
import json


class FileStorage:
    """
    Represent an abstracted storage engine.

    Attr:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file 
        """
        data_to_save = {key: value.__dict__ for key, value in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data_to_save, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if it exists.
        """
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    FileStorage.__objects = json.load(file)
                    for v in FileStorage.__objects.items():
                        className = v["__class__"]
                        # using the eval function to dynamically create an instance of a class based on the class name
                        FileStorage.new(eval(className)(**v))
            except FileNotFoundError:
                pass

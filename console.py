#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from zeyad.models.base_model import BaseModel
from __init__ import storage



class HBNBCommand(cmd.Cmd):
    """

    """
    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
    }

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Overriding emptyline method from cmd module so that
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        print() # Print a newline before exiting
        return True

    def do_create(self, line):
        """
        Create a new instance.
        """
        # parseline to extract the class name from the user input and then attempts to create an instance of that class.
        class_name = self.parseline(line)[0]

        if class_name is None:
             print("** class name missing **")
        elif class_name not in globals():
             print("** class doesn't exist **")
        else:
            ###
            # globals is a function returns a dictionary. The keys are the names of all global 
            # variables, functions, classes in the current moment. and the values are the class itself.
            # dictionary[key] -> value ((value = class))
            # dictionary["BaseModel"] = BaseModel()
            # instance = class()
            # new_instance = globals()[class_name]()
            new_instance = globals()[class_name]()

            ###
            # Note that we can NOT use eval() here becuase eval takes a string containing a dictionary 
            # that has the attributes of the instance we want to create and therefore we can't use it with 
            # class_name because it's a string that has only the name
            print(new_instance.id)

            ###
            # the new_instance is already added to the FileStorage.__objects when the instance was initially created
            # and the call to save here just saves what's in there to the storage space
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

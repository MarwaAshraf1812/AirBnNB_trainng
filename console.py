#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
#from models.base_model import BaseModel
#from models import storage



class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb)"

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
        #parseline to extract the class name from the user input and then attempts to create an instance of that class.

        class_name = self.parseline(line)[0]

        if class_name is None:
             print("** class name missing **")
        elif class_name not in self.__classes:
             print("** class doesn't exist **")
        else:
            print(eval(class_name).id)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

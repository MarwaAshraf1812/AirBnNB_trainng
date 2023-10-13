# import cmd

# class MyCmd(cmd.Cmd):
#     def __init__(self):
#         super().__init__()
#         self.custom_stop_condition = False

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

#     def postcmd(self, stop, line):
#         """Print a message after each command"""
#         if self.custom_stop_condition:
#             print("Exiting the command loop. Goodbye!")
#             return True  # This stops the command loop
#         else:
#             print("Command executed successfully.")
#             return False  # This allows the command loop to continue

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()
#     my_cmd_instance.cmdloop(intro="Welcome to My Interactive Shell. Type 'help' for help.")





# import cmd

# class MyCmd(cmd.Cmd):
#     # Setting custom identification characters
#     identchars = cmd.Cmd.identchars + '_'

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Starting the command loop
#     my_cmd_instance.cmdloop()


# import cmd

# class MyCmd(cmd.Cmd):
#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

#     def do_repeat(self, arg):
#         """Repeat the last command."""
#         last_command = self.lastcmd
#         if last_command:
#             print(f"Repeating: {last_command}")
#             self.onecmd(last_command)
#         else:
#             print("No previous command to repeat.")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Starting the command loop
#     my_cmd_instance.cmdloop()


# import cmd

# class MyCmd(cmd.Cmd):
#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Queueing up commands
#     my_cmd_instance.cmdqueue.extend(["hello Alice", "hello Bob", "hello Charlie"])

#     # Starting the command loop
#     my_cmd_instance.cmdloop()


# import cmd

# class MyCmd(cmd.Cmd):
#     # Setting a custom miscellaneous help header
#     misc_header = "Additional Help Topics"

#     def help_example(self):
#         """Provide help for the 'example' topic."""
#         print("This is help for the 'example' topic.")

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Starting the command loop
#     my_cmd_instance.cmdloop()


# import cmd

# class MyCmd(cmd.Cmd):
#     # Setting a custom undocumented commands header
#     undoc_header = "Undocumented Commands"

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Starting the command loop
#     my_cmd_instance.cmdloop()


# import cmd

# class MyCmd(cmd.Cmd):
#     # Setting a custom ruler character
#     ruler = '-'

#     def help_hello(self):
#         """Provide help for the 'hello' command."""
#         print("This is help for the 'hello' command.")

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Starting the command loop
#     my_cmd_instance.cmdloop()


# import cmd

# class MyCmd(cmd.Cmd):
#     # Setting use_rawinput to False
#     use_rawinput = False

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Starting the command loop
#     my_cmd_instance.cmdloop()


# import cmd

# class HelloWorld(cmd.Cmd):
#     """Simple command processor example."""
    
#     def do_greet(self, line):
#         print("hello")
    
#     def do_EOF(self, line):
#         return True

# if __name__ == '__main__':
#     HelloWorld().cmdloop()


# import cmd

# class HelloWorld(cmd.Cmd):
#     """Simple command processor example."""
    
#     def do_greet(self, person):
#         """greet [person]
#         Greet the named person"""
#         if person:
#             print ("hi, " + person)
#         else:
#             print('hi')
    
#     def do_EOF(self, line):
#         return True
    
#     def postloop(self):
#         print

# if __name__ == '__main__':
#     HelloWorld().cmdloop()

# import cmd

# class HelloWorld(cmd.Cmd):
#     """Simple command processor example."""
    
#     def do_greet(self, person):
#         if person:
#             print ("hi,"  + person)
#         else:
#             print ("hi")
    
#     def help_greet(self):
#         print("greet [person]"+ "\n" +"Greet the named person")

#     def do_EOF(self, line):
#         return True

# if __name__ == '__main__':
#     HelloWorld().cmdloop()

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    
    def do_greet(self, person):
        "Greet the person"
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = 'hello'
        print (greeting)
    
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
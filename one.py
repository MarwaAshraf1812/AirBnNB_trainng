# import cmd

# class MyCmd(cmd.Cmd):
#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Using onecmd to execute a command
#     my_cmd_instance.onecmd("hello Alice")


# import cmd

# class MyCmd(cmd.Cmd):
#     def precmd(self, line):
#         """Add a prefix to each command before execution"""
#         return f"prefix_{line}"

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Using the overridden precmd method
#     my_cmd_instance.onecmd("hello Alice")



# import cmd

# class MyCmd(cmd.Cmd):
#     def precmd(self, line):
#         """Convert the command to uppercase before execution."""

#         return line.upper()

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Using the overridden precmd method
#     my_cmd_instance.onecmd("hello Alice")


# import cmd

# class MyCmd(cmd.Cmd):
#     def emptyline(self):
#         """Action to take when the user presses Enter without typing a command."""
#         print("You pressed Enter. Type a command or 'help' for assistance.")

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Pressing Enter without typing a command
#     my_cmd_instance.onecmd("")


# import cmd

# class MyCmd(cmd.Cmd):
#     def default(self, line):
#         """Action to take when the user types an unrecognized command."""
#         print(f"Unknown command: {line}. Type 'help' for assistance.")

#     def do_hello(self, arg):
#         """Say hello to someone: hello [name]"""
#         print(f"Hello, {arg or 'stranger'}!")

# if __name__ == "__main__":
#     my_cmd_instance = MyCmd()

#     # Typing an unknown command
#     my_cmd_instance.onecmd("unknown_command")


import cmd

class MyCmd(cmd.Cmd):
    def completedefault(self, text, line, begidx, endidx):
        """Custom autocomplete for any command starting with 'greet'."""
        if text.startswith("greet"):
            return ["greet"]
        else:
            return []

    def do_greet(self, arg):
        """Greet someone: greet [name]"""
        print(f"Hello, {arg or 'stranger'}!")

if __name__ == "__main__":
    my_cmd_instance = MyCmd()

    # Trying autocompletion with an unknown command
    my_cmd_instance.completedefault("g", "g", 0, 0)

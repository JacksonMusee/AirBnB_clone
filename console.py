#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    AirBnB command interpreter class
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """
        Do nothing is line is empty
        """
        pass

    def do_EOF(self, line):
        """
        Exit properly at end of file
        """
        return (True)

    def do_quit(self, line):
        """
        Exit on quit
        """
        return (True)

    def help_quit(self):
        """
        help quit
        """
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

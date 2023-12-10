#!/usr/bin/python3
""" Console Module """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def do_quit(self, comand):
        """Quit command to exit the program"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF  """
        print("Exits the program without  formatting\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

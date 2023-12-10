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

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

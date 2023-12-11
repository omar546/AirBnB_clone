#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review, }

    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def do_quit(self, comand):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """ Prints the help documentation for quit"""
        print("Exits the program with formatting")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        return True

    def help_EOF(self):
        """ Prints the help documentation for EOF  """
        print("Exits the program without formatting")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ create a mew model and saves it in the JSON file"""
        if (not args):
            print("** class name missing **")
            return
        elif (args not in self.classes):
            print("** class doesn't exist **")
            return
        else:
            temp = self.classes[args]()

            storage.new(temp)
            storage.save()
            print(temp.id)
            temp.save()

    def help_create():
        """Prints the help document for the create"""
        print("create a mew model and saves it in the JSON file")

    def do_show(self, args):
        new = args.partition(" ")

        class_name = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]

        if (not class_name):
            print("** class name missing **")
            return
        elif (not class_id):
            print("** instance id missing **")
            return
        elif (class_name not in self.classes):
            print("** class doesn't exist **")
            return
        else:
            try:
                all = storage.all()
                our_id = f"{class_name}.{class_id}"
                t = all[our_id]
                print(all[our_id])
            except KeyError:
                print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        new = args.partition(" ")

        class_name = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]

        if (not class_name):
            print("** class name missing **")
            return
        elif (not class_id):
            print("** instance id missing **")
            return
        elif (class_name not in self.classes):
            print("** class doesn't exist **")
            return
        else:
            try:
                our_id = f"{class_name}.{class_id}"
                del (storage.all()[our_id])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        if (not args):
            print(storage.all())
            return
        elif (args not in self.classes):
            print("** class doesn't exist **")
            return
        else:
            return_list = []

            for key, value in storage.all().items():
                temp = key.split(".")[0]
                if temp == args:
                    return_list.append(str(value))
            print(return_list)

    
    def do_update(self, args):
        """
        Usage: Usage: update <class> <id> <attribute_name> <attribute_value>
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = args.split()
        all = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in all:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            our_object = all[f"{args[0]}.{args[1]}"]
            if args[2] in our_object.__dict__.keys():
                val_type = type(our_object.__dict__[args[2]])
                our_object.__dict__[args[2]] = val_type(args[3])
            else:
                our_object.__dict__[args[2]] = args[3]
            storage.save()
            our_object.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

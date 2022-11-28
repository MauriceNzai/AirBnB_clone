#!/usr/bin/python3
"""
This module is the entry point of the program through the class HBNBCommand

Created on Tue Nov 22, 2022

@authors: Maurice Haro
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    is the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    class_list = [
            "BaseModel", 'User', 'State', 'City',
            'Amenity', 'Place', 'Review']

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        print()
        return True

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        defines what to execute in case of am empty line
        """
        pass

    def postloop(self):
        """
        defines what the program does after each console loop
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of the BaseModel class,
        saves it to JSON file and print the id
        """
        line = args.split()
        if not self.verify_class(line):
            return
        this_obj = eval(line[0] + '()')
        if isinstance(this_obj, BaseModel):
            this_obj.save()
            print(this_obj.id)
        return

    def do_show(self, args):
        """
        prints the string representation of an object based on class name & id
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return

        objects = models.storage.all()
        this_obj_id = '{}.{}'.format(line[0], line[1])
        print(objects[this_obj_id])

    def do_destroy(self, args):
        """
        deletes an object based on theclass name and id
        and saves changes to JSON file
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return

        objects = models.storage.all()
        this_obj_id = "{}.{}".format(line[0], line[1])
        del objects[this_obj_id]
        models.storage.save()

    def do_all(self, args):
        """
        prints the string representations of all abojects
        based on or not on the class name
        """
        line = args.split()
        objects = models.storage.all()
        objs_to_print = []
        if len(line) == 0:
            for value in objects.values():
                objs_to_print.append(str(value))
        elif line[0] in HBNBCommand.class_list:
            for key, value in objects.items():
                if line[0] in key:
                    objs_to_print.append(str(value))
        else:
            print("** class doesn't exist **")
            return False

        print(objs_to_print)

    def do_update(self, args):
        """
        updates an object based on the class name and id by adding or updating
        attribute, and save the changes to the JSON file
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        if not self.verify_attribute(line):
            return
        objects = models.storage.all()
        this_obj_id = "{}.{}".format(line[0], line[1])
        setattr(objects[this_obj_id], line[2], line[3])
        models.storage.save()

    def do_count(self, args):
        """
        Tracks the number of instances of a given class
        """
        line = args.split()
        count = 0
        for obj in models.storage.all().values():
            if line[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, args):
        """
        default method called when the command input starts with a class name
        """
        line = args.strip('()').split(".")
        if len(line) < 2:
            print("** missing attribute **")
            return

        objects = models.storage.all()
        class_name = line[0].capitalize()
        cmd_name = line[1].lower()
        split2 = cmd_name.strip(')').split('(')
        cmd_name == split2[0]

        if cmd_name == "all":
            HBNBCommand.do_all(self, class_name)
        elif cmd_name == "count":
            HBNBCommand.do_count(self, class_name)

        elif cmd_name == "show":
            if len(split2) < 2:
                print("** no instance found **")
            else:
                HBNBCommand.do_show(self, class_name + ' ' + split2[1])
        elif cmd_name == "destroy":
            if len(split2) < 2:
                print("** no instance found **")
            else:
                HBNBCommand.do_destroy(self, class_name + ' ' + split2[1])
        elif cmd_name == "update":
            split3 = split2[1].split(', ')
            if len(split3) == 0:
                print("** no instance found **")
            elif len(split3) == 1 and type(split3[1]) == dict:
                for key, value in split[1].items():
                    HBNBCommand.do_update(
                            self, class_name + " " + split3[0] +
                            " " + key + " " + value)
            elif len(split3) == 1 and type(split3[1]) != dict:
                print("** no instance found **")
            elif len(split3) == 2:
                print("** no instance found **")
            else:
                HBNBCommand.do_update(
                        self, class_name + " " + split3[0] + " " +
                        split3[1] + " " + split3[2])

    @classmethod
    def verify_class(cls, line):
        """
        verifies the input class name
        """
        if len(line) == 0:
            print("** class does\'nt exist **")
            return False
        elif line[0] not in HBNBCommand.class_list:
            print("** class doesn\'t exist **")
            return False
        return True

    @staticmethod
    def verify_id(line):
        """
        verifies the id input
        """
        if len(line) < 2:
            print("** instance id missing **")
            return False

        objects = models.storage.all()
        key = "{}.{}".format(line[0], line[1])
        if key not in objects.keys():
            print("** no instance found **")
            return False
        return True

    @staticmethod
    def verify_attribute(line):
        """
        verifies attribute in line input
        """
        if len(line) < 3:
            print("** attribute name Missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

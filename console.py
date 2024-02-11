#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""

import cmd
import importlib


class HBNBCommand(cmd.Cmd):
    """
    AirBnB command interpreter class
    """

    prompt = '(hbnb) '

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        If the class name is missing, print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        """
        if not line:
            print("** class name missing **")

        else:
            cls_name = line.split()[0]
            modules = ["models.base_model"]

            for item in modules:
                module = importlib.import_module(item)
                if hasattr(module, cls_name):
                    new_instance = getattr(module, cls_name)()
                    new_instance.save()
                    print(new_instance.id)
                    return

            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing ** (ex: $ show)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
                return
            cls_name = args[0]
            obj_id = args[1]
            modules = ["models.base_model", "models.engine.file_storage"]

            for item in modules:
                module = importlib.import_module(item)
                if hasattr(module, cls_name):
                    storage = module.storage
                    all_objs_dict = storage.all()

                    key = f"{cls_name}.{obj_id}"

                    if key in all_objs_dict:
                        print(all_objs_dict[key])
                        return
                    else:
                        print("** no instance found **")
                        return

            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ destroy)
If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
                return
            cls_name = args[0]
            obj_id = args[1]
            modules = ["models.base_model", "models.engine.file_storage"]

            for item in modules:
                module = importlib.import_module(item)
                if hasattr(module, cls_name):
                    storage = module.storage
                    all_objs_dict = storage.all()

                    key = f"{cls_name}.{obj_id}"

                    if key in all_objs_dict:
                        del all_objs_dict[key]
                        storage.save()
                        return
                    else:
                        print("** no instance found **")
                        return

            print("** class doesn't exist **")


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

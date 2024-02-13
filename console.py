#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""

import cmd
import importlib

model_list = ["models.base_model", "model.user", "models.engine.file_storage"]

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
            modules = model_list

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
            modules = model_list

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
            modules = model_list

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

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
        """
        instance_list = []
        modules = model_list

        if line:
            cls_name = line.split()[0]

            for item in modules:
                module = importlib.import_module(item)
                if hasattr(module, cls_name):
                    storage = module.storage
                    all_objs_dict = storage.all()

                    for key, value in all_objs_dict.items():
                        if key.startswith(cls_name + "."):
                            instance_list.append(value.__str__())
                    print(instance_list)
                    return
            print("** class doesn't exist **")

        else:
            for item in modules:
                module = importlib.import_module(item)
                storage = module.storage
                all_objs_dict = storage.all()

                for key, value in all_objs_dict.items():
                    instance_list.append(value.__str__())
                print(instance_list)
                return

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = line.split()
        args_len = len(args)

        if (args_len == 3):
            print("** value missing **")
            return
        if (args_len == 2):
            print("** attribute name missing **")
            return
        if (args_len == 1):
            print("** instance id missing **")
            return
        if (args_len == 0):
            print("** class name missing **")
            return

        cls_name = args[0]
        insta_id = args[1]
        attr_name = args[2]
        attr_val = args[3]
        modules = model_list
        
        for item in modules:
            module = importlib.import_module(item)

            if hasattr(module, cls_name):
                storage = module.storage
                all_objs_dict = storage.all()

                key = f"{cls_name}.{insta_id}"
                if key in all_objs_dict:
                    target_obj = all_objs_dict[key]
                    if hasattr(target_obj, attr_name):
                        its_type = type(getattr(target_obj, attr_name))
                        setattr(target_obj, attr_name, its_type(attr_val.strip('"')))
                        storage.save()
                    else:
                        setattr(target_obj, attr_name, attr_val.strip('"'))
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

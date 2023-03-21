#!/usr/bin/python3
"""engine to run our program from the console"""
import cmd
import sys
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

"""parse the arguments into a list"""


def parse(arg):
    """splits the arguments"""
    brace = re.search(r"\{(.*?)\}", arg)
    brack = re.search(r"\[(.*?)\]", arg)
    if brace is None:
        if brack is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:brack.span()[0]])
            ret = [i.strip(",") for i in lex]
            ret.append(brack.group())
            return ret
    else:
        lex = split(arg[:brace.span()[0]])
        ret = [i.strip(",") for i in lex]
        ret.append(brace.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """here we will add methods in order to run all the basic
    commands on the project
    We shall use our own personal prompt
    """

    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_EOF(self, line):
        """to catch the end of file and control+ D"""
        return True

    def do_quit(self, line):
        """the quit command should exit the programe"""
        sys.exit(1)

    def emptyline(self):
        """overide new line to not execute anything"""
        pass

    def do_create(self, args):
        """creates a new instance of BaseModel"""
        arg1 = parse(args)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def do_show(self, args):
        """Prints the string representation of an instance"""
        arg1 = parse(args)
        obj = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj:
            print("** no instance found **")
        else:
            print(obj["{}.{}".format(arg1[0], arg1[1])])

    def do_destroy(self, args):
        """destroy or delete an instance of a class"""
        arg = parse(args)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj.keys():
            print("** no instance found **")
        else:
            del(obj["{}.{}".format(arg[0], arg[1])])
            storage.save()

    def do_all(self, args):
        """print a list of all available instances of a class"""
        arg = parse(args)
        obj = storage.all()
        ls = []
        if len(arg) > 0 and arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for ob in obj.values():
                if len(arg) > 0 and arg[0] == ob.__class__.__name__:
                    ls.append(ob.__str__())
                elif len(arg) == 0:
                    ls.append(ob.__str__())
            print(ls)

    def do_update(self, args):
        """updates an instance based on class name and id"""
        arg = parse(args)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in self.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg[0], arg[1]) not in obj:
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            False
        if len(arg) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
            return False
        if len(arg) == 4:
            key = obj["{}.{}".format(arg[0], arg[1])]
            if arg[2] in key.__class__.__dict__.keys():
                valtp = type(key.__class__.__dict__[arg[2]])
                key.__dict__[arg[2]] = valtp(arg[3])
            else:
                key.__dict__[arg[2]] = arg[3]
        elif type(eval(arg[2])) == dict:
            key = obj["{}.{}".format(arg[0], arg[1])]
            for ke, val in eval(arg[2]).items():
                if (ke in key.__class__.__dict__.keys() and
                   type(key.__class__.__dict__[ke] in [str, int, float])):
                    valtp = type(key.__class__.__dict__[ke])
                    obj.__dit__[ke] = valtp(val)
                else:
                    key.__dict__[ke] = val

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

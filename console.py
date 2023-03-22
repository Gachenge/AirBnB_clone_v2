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
        try:
            if not args:
                raise SyntaxError()
            nlist = args.split(" ")

            news = {}
            for i in range(1, len(news)):
                key, value = tuple(news[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                news[key] = value

            if news == {}:
                obj = eval(nlist[0])()
            else:
                obj = eval(nlist[0])(**news)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        try:
            if not args:
                raise SyntaxError()
            nlist = args.split(" ")
            if nlist[0] not in self.__classes:
                raise NameError()
            if len(nlist) < 2:
                raise IndexError()
            news = storage.all()
            key = news[0] + '.' + nlist[1]
            if key in news:
                print(news[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """destroy or delete an instance of a class"""
        try:
            if not args:
                raise SyntaxError()
            nlist = args.split(" ")
            if nlist[0] not in self.__classes:
                raise NameError()
            if len(nlist) < 2:
                raise IndexError()
            news = storage.all()
            key = nlist[0] + '.' + nlist[1]
            if key in news:
                del news[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """print a list of all available instances of a class"""
        if not args:
            obj = storage.all()
            print([obj[key].__str__() for key in obj])
            return
        try:
            arg = args.split(" ")
            if arg[0] not in self.__classes:
                raise NameError()

            new = eval(arg[0])
            obj = storage.all(new)
            print([obj[key].__str__() for key in obj])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        """updates an instance based on class name and id"""
        try:
            if not args:
                raise SyntaxError()
            nlist = args.split(" ")
            if nlist[0] not in self.__classes:
                raise NameError()
            if len(nlist) < 2:
                raise IndexError()
            obj = storage.all()
            key = nlist[0] + '.' + nlist[1]
            if key not in obj:
                raise KeyError()
            if len(nlist) < 3:
                raise AttributeError()
            if len(nlist) < 4:
                raise ValueError()
            value = obj[key]
            try:
                value.__dict__[nlist[2]] = eval(nlist[3])
            except Exception:
                value.__dict__[nlist[2]] = nlist[3]
                value.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def strip(self, args):
        """strips the arguments and return a string"""
        nlist = []
        nlist.append(args[0])
        try:
            mydict = eval(args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            mydict = None
        if type(mydict) == dict:
            stri = args[1][args[1].find('(')+1:args[1].find(')')]
            nlist.append((stri.split(', '))[0]).strip('"')
            nlist.append(mydict)
            return nlist
        stri = args[1][args[1].find('(')+1:args[1].find(')')]
        nlist.append(" ".join(stri.split(", ")))
        return " ".join(i for i in nlist)

    def default(self, args):
        """default case"""
        nlist = args.split('.')
        if len(nlist) >= 2:
            if (nlist[1] == "all()"):
                self.do_all(nlist[0])
            elif nlist[1][:4] == "show":
                self.do_show(self.strip(nlist))
            elif nlist[1][:7] == "destroy":
                self.do_destroy(self.strip(nlist))
            elif nlist[1][:6] == "update":
                args = self.strip(nlist)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for key, value in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(key, value))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

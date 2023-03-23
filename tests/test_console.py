#!/usr/bin/python3
"""unittests for console.py"""
import pep8
import os
import unittest
import models
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """testing the command interpretor"""

    def test_pep8(self):
        """test pycodestyle"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, "fix Pep8")

    def test_docstrings(self):
        """check for documentation"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_help.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_EOF(self):
        """tests that EOF quits"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB = HBNBCommand()
            self.assertTrue(HBNB.onecmd("EOF"))

    def test_quit(self):
        """tests the quit command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB = HBNBCommand()
            self.assertEqual("", f.getvalue())

    def test_emptyline(self):
        """empty line should just skip"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB = HBNBCommand()
            HBNB.onecmd('\n')
            self.assertEqual("", f.getvalue())

    def test_create_excep(self):
        """test if exceptions are caught"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB = HBNBCommand()
            HBNB.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create cow")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_show(self):
        """test show command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB = HBNBCommand()
            HBNB.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("show cow")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("show User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("show BaseModel cow")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """test the destroy command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB = HBNBCommand()
            HBNB.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("destroy cow")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("destroy BaseModel cow")
            self.assertEqual("** no instance found **\n", f.getvalue())


if __name__ == "__main__":
    unittest.main()

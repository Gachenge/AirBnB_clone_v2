#!/usr/bin/python3

import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

"""unittests for the file storage class"""


class TestFile(unittest.TestCase):
    """tests all methods of the file storage"""
    def test_filepath(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects(self):
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_noarg(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_onearg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all(self):
        a = FileStorage()
        self.assertEqual(a.all(), FileStorage._FileStorage__objects)

    def test_new(self):
        a = BaseModel()
        self.assertIn(a.__class__.__name__ + '.' + a.id,
                      models.storage.all().keys())

    def test_new_no_arg(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        self.assertEqual(type('file.json'), str)

    def test_reload_nonearg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_savno(self):
        a = BaseModel()
        models.storage.new(a)
        models.storage.save()
        with open("file.json") as f:
            self.assertIn("BaseModel." + a.id, f.read())

    def test_rl(self):
        a = FileStorage()
        with open('file.json', 'w') as f:
            f.write("{}")
        with open('file.json') as f:
            for i in f:
                self.assertEqual(i, "{}")
        self.assertIs(a.reload(), None)


if __name__ == '__main__':
    unittest.main()

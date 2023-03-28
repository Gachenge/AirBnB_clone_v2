#!/usr/bin/python3
""" testing Place """
import unittest
import pep8
from models.place import Place


class test_place(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/place.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()

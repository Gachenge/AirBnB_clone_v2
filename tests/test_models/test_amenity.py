#!/usr/bin/python3
""" testing Amenity """
import unittest
import pep8
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc(self):
        """check for documentation"""
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == '__main__':
    unittest.main()

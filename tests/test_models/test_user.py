#!/usr/bin/python3
""" testing User """
import unittest
import pep8
from models.user import User


class User_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/user.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_umail(self):
        self.assertEqual(type(User().email), str)

    def test_pass(self):
        self.assertEqual(type(User().password), str)

    def test_fname(self):
        self.assertEqual(type(User().first_name), str)

    def test_lname(self):
        self.assertEqual(type(User().last_name), str)


if __name__ == "__main__":
    unittest.main()

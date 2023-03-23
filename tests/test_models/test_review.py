#!/usr/bin/python3
""" testing Review """
import unittest
import pep8
from models.review import Review


class Review_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/review.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pid(self):
        self.assertEqual(type(Review().place_id), str)

    def test_uid(self):
        self.assertEqual(type(Review().user_id), str)

    def test_text(self):
        self.assertEqual(type(Review().text), str)


if __name__ == "__main__":
    unittest.main()

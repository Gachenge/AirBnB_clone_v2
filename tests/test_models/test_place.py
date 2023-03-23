#!/usr/bin/python3
""" testing Place """
import unittest
import pep8
from models.place import Place


class Place_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/place.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_cid(self):
        self.assertEqual(type(Place().city_id), str)

    def test_uid(self):
        self.assertEqual(type(Place().user_id), str)

    def test_name(self):
        self.assertEqual(type(Place().name), str)

    def test_description(self):
        self.assertEqual(type(Place().description), str)

    def test_nuroom(self):
        self.assertEqual(type(Place().number_rooms), int)

    def test_nubath(self):
        self.assertEqual(type(Place().number_bathrooms), int)

    def test_maxgu(self):
        self.assertEqual(type(Place().max_guest), int)

    def test_pric(self):
        self.assertEqual(type(Place().price_by_night), int)

    def test_lat(self):
        self.assertEqual(type(Place().latitude), float)

    def test_lon(self):
        self.assertEqual(type(Place().longitude), float)

    def test_amenid(self):
        self.assertEqual(type(Place().amenity_ids), list)


if __name__ == "__main__":
    unittest.main()

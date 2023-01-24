#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Initialization(unittest.TestCase):
    """Testing Initialization of the Base Class"""

    def test_no_args(self):
        """Test id with no arguments"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)

    def test_multiple_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        self.assertNotEqual(b1.id, b2.id)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertIsNotNone(b1.id)
        self.assertIsNotNone(b2.id)
        self.assertEqual(b1.id, b2.id -1)

    def test_Base_89(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

class TestBase_to_json_string(unittest.TestCase):

    def test_type(self):
        b1 = Rectangle(10,7,2,8)
        dictionary = b1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str, type(json_dictionary))

    def test_empty_list(self):
        self.assertEqual('[]', Base.to_json_string([]))

    def test_no_args_None(self):
        self.assertEqual('[]', Base.to_json_string(None))

    def test_empty_string_list(self):
        self.assertEqual('"[]"', Base.to_json_string("[]"))

    def test_dict_args(self):
        json_dictionary = Base.to_json_string([{"id":12}])
        self.assertEqual('[{"id": 12}]', json_dictionary)


class TestBase_from_json_string(unittest.TestCase):

    def test_empty_json_string_or_None(self):
        self.assertEqual([], Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string("[]"))

    def test_id_args(self):
        self.assertEqual([{ "id": 89 }],
                         Base.from_json_string('[{ "id": 89 }]'))
        
if __name__ == "__main__":
    unittest.main()

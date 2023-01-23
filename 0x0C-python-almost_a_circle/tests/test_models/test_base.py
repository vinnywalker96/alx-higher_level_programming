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


if __name__ == "__main__":
    unittest.main()

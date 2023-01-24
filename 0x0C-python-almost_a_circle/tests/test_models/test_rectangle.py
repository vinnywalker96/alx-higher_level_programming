#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_initialization(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10,2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

class TestRectangle_area(unittest.TestCase):
    """Test Area"""

    def test_area_args(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(2, r1.area())
        
if __name__ == "__main__":
    unittest.main()

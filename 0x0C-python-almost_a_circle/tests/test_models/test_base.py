#!/usr/bin/python3
"""
Defines base test case
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_Class(unittest.TestCase):
     """Unittests for testing instantiation of the Base class."""

     def test_no_args(self):
         b1 = Base()
         b2 = Base()
         self.assertEqual(b1.id, b2.id -1)

     def test_id(self):
          b1 = Base(None)
          b2 = Base(None)
          self.assertEqual(b1.id, b2.id - 1)

     def test_unique_id(self):
          self.assertEqual(12, Base(12).id)
          
if __name__ == "__main__":
    unittest.main()

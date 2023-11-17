#!/usr/bin/python3
"""Unit testing class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Testing class Rectangle"""

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(8, 2, 0, 0, 12)
        self.r3 = Rectangle(8, 21, 4, 3, -6)
        self.r4 = Rectangle(7, 5, 2, 6)

    def test_width(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 8)
        self.assertEqual(self.r3.width, 8)
        self.assertEqual(self.r4.width, 7)
        with self.assertRaises(ValueError):
            Rectangle(0, 4)
            Rectangle(-3, 2, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle("Hello", 8)

    def test_height(self):
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r3.height, 21)
        self.assertEqual(self.r4.height, 5)
        with self.assertRaises(ValueError):
            Rectangle(4, 0)
            Rectangle(3, -2, 1, 2)
        with self.assertRaises(TypeError):
            Rectangle(8, "Hello")
            Rectangle(8, 2.2)

    def test_x(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 4)
        self.assertEqual(self.r4.x, 2)
        with self.assertRaises(ValueError):
            Rectangle(4, 1, -3)
        with self.assertRaises(TypeError):
            Rectangle(3, 2, "Hi")
            Rectangle(3, 2, 7.3)

    def test_y(self):
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 3)
        self.assertEqual(self.r4.y, 6)
        with self.assertRaises(ValueError):
            Rectangle(4, 1, 3, -2)
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 7, 4.5)
            Rectangle(3, 2, 7, "i")

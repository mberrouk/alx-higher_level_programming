#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):


    def test_base_noArg(self):
        bbase1 = Base()
        bbase2 = Base()
        bbase3 = Base()
        self.assertEqual(bbase1.id, 1, "id for base1 is 1")
        self.assertEqual(bbase2.id, 2, "id for base2 is 2")
        self.assertEqual(bbase3.id, 3, "id for base3 is 3")

    def test_base_arg(self):
        base100 = Base(100)
        base0 = Base(00)
        basen10 = Base(-10)
        self.assertEqual(base100.id, 100, "id for base100 is 100")
        self.assertEqual(base0.id, 0, "id for base0 is 0")
        self.assertEqual(basen10.id, -10, "id for basen10 is -10")

    def test_base_arg_noArg(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b100 = Base(100)
        b2 = Base()
        b0 = Base(00)
        b3 = Base()
        bn10 = Base(-10)
        self.assertEqual(b1.id, 1, "id for b1 is 1")
        self.assertEqual(b100.id, 100, "id for b100 is 100")
        self.assertEqual(b2.id, 2, "id for b2 is 2")
        self.assertEqual(b0.id, 0, "id for b0 is 0")
        self.assertEqual(b3.id, 3, "id for b3 is 3")
        self.assertEqual(bn10.id, -10, "id for bn10 is -10")

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Unittest for Square class
"""
import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):

    def test_CreateClass(self):
        s1 = Square(10)
        self.assertAlmostEqual(s1.width, 10)
        self.assertAlmostEqual(s1.id, 5)
        with self.assertRaises(TypeError):
            Square("10")
        with self.assertRaises(ValueError):
            Square(-1)

    def test_Size(self):
        s2 = Square(10)
        self.assertAlmostEqual(s2.size, 10)
        self.assertAlmostEqual(s2.id, 6)

    def test_Print(self):
        s3 = Square(4, 2, 1, 12)
        self.assertAlmostEqual(Square.__str__(
            s3), "[Square] (12) 2/1 - 4")

    def test_Update(self):
        r1 = Square(10, 10, 10, 10)
        self.assertAlmostEqual(Square.__str__(
            r1), "[Square] (10) 10/10 - 10")
        r1.update(89, 2, 4, 5)
        self.assertAlmostEqual(Square.__str__(
            r1), "[Square] (89) 4/5 - 2")

        r2 = Square(10, 10, 10, 10)
        self.assertAlmostEqual(Square.__str__(
            r2), "[Square] (10) 10/10 - 10")
        r2.update(x=1, y=3, size=4, id=89)
        self.assertAlmostEqual(Square.__str__(
            r2), "[Square] (89) 1/3 - 4")

    def test_ToDict(self):
        s4 = Square(10, 2, 1, 9)
        s4_dictionary = s4.to_dictionary()
        self.assertAlmostEqual(
            type(s4_dictionary), dict)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_CreateClass(self):
        r1 = Rectangle(10, 2)
        self.assertAlmostEqual(r1.width, 10)
        self.assertAlmostEqual(r1.height, 2)
        self.assertAlmostEqual(r1.id, 3)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -1)
            Rectangle(-1, 10)

    def test_Area(self):
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertAlmostEqual(r1.area(), 56)

    def test_Print(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_Update(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (10) 10/10 - 10/10")
        r1.update(89, 2, 3, 4, 5)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (89) 4/5 - 2/3")

        r2 = Rectangle(10, 10, 10, 10, 10)
        self.assertAlmostEqual(Rectangle.__str__(
            r2), "[Rectangle] (10) 10/10 - 10/10")
        r2.update(x=1, height=2, y=3, width=4, id=89)
        self.assertAlmostEqual(Rectangle.__str__(
            r2), "[Rectangle] (89) 1/3 - 4/2")

    def test_ToDict(self):
        r4 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r4.to_dictionary()
        self.assertAlmostEqual(
            type(r1_dictionary), dict)


if __name__ == "__main__":
    unittest.main()

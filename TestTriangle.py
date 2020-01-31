# -*- coding: utf-8 -*-
"""
Updates on Friday January 31 2020

@author: Varun Mark Mullins
cwid:10456027

This file takes in three lengths of a triangle and checks the validity of the triangle and returns the type of
triangle and checks if it is a right angle triangle or not.

"""

import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    """Tests for checking the Triangle file"""

    def testValid1(self):
        """Test for input above 200"""
        self.assertEqual(classifyTriangle(201, 0, 4), 'InvalidInput')

    def testValid2(self):
        """Test for input less than or equal to 0"""
        self.assertEqual(classifyTriangle(-1, 0, 6), 'InvalidInput')

    def testValidInp(self):
        """Test for input not an integer"""
        self.assertEqual(classifyTriangle('a', 'b', 2), 'InvalidInput')

    def triangleTest(self):
        """Test to check the validity of the triangle"""
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle')

    def testRightTriangleA(self):
        """Test if the triangle is a right angle Triangle"""
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        """Test if the triangle is a right angle Triangle"""
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def testEquilateralTriangles(self):
        """Test if the triangle is an Equilateral Triangle"""
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testIsoscelesTriangles(self):
        """Test if the triangle is an Isosceles Triangle"""
        self.assertEqual(classifyTriangle(1, 3, 3), 'Isoceles')

    def testScaleneTriangles(self):
        """Test if the triangle is a Scalene Triangle"""
        self.assertEqual(classifyTriangle(1, 3, 4), 'Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

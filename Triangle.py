# -*- coding: utf-8 -*-
"""
Updates on Friday January 31 2020

@author: Varun Mark Mullins
cwid:10456027

This file takes in three lengths of a triangle and checks the validity of the triangle and returns the type of
triangle and checks if it is a right angle triangle or not.
"""


def classifyTriangle(a, b, c):
    """Function checks the type of triangle"""
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        """Checks if the input is valid"""
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        """Checks if the input is within 200"""
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        """Returns an invalid input if the input is negative or zero"""
        return 'InvalidInput'

    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
        """Checks if the triangle is a valid triangle or not"""
        return 'NotATriangle'

    # now we know that we have a valid triangle 
    if a == b and b == c:
        """If triangle is Equilateral"""
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2) or ((a ** 2) + (c ** 2)) == (a ** 2):
        """If not equilateral but a right angle triangle"""
        return 'Right'
    elif (a != b) and (b != c):
        """If the triangle is scalene"""
        return 'Scalene'
    else:
        """If the triangle is Isosceles"""
        return 'Isosceles'

from triangle import RightTriangle
import pytest
import math

def equals_float(a, b, epsilon=0.05):
    """ Determine if two floating-point values are 
        equal to two decimal places """
    return abs(a - b) <= epsilon 

# Write your tests here

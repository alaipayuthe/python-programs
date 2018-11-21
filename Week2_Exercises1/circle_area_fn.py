"""
Write a Python function circle_area that takes a single parameter radius corresponding to the radius of a circle in inches and returns the the area of a circle with radius in square inches. Do not use π=3.14, instead use the math module to supply a higher-precision approximation to π. Area of circle template --- Area of circle solution
"""

import math

def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

print("Area of circle with 5 inches as radius: " + str(circle_area(5)) + " square inches")

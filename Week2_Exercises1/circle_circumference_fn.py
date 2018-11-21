"""
Write a Python function circle_circumference that takes a single parameter radius corresponding to the radius of a circle in inches and returns the the circumference of a circle with radius  in inches. Do not use π=3.14, instead use the math module to supply a higher-precision approximation to π. Circumference of circle template --- Circumference of circle solution
"""

import math

def circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

print("Circle circumference of radius 6 inches: " + str(circle_circumference(6)) + " inches")

"""
Write a Python function point_distance that takes as input the parameters x_0, y_0, x_1 and y_1, and returns the distance between the points (x0,y0) and (x1,y1). Point distance template --- Point distance solution
"""

import math
def point_distance(x0, y0, x1, y1):
    distance = math.sqrt(((x0 - x1) ** 2) + ((y0 -y1) ** 2))
    return distance

print("Distance between points (1, 2) and (3, 4) : " + str(point_distance(1, 2, 3, 4)))


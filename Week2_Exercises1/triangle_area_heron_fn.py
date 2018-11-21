"""
Challenge: Write a Python function triangle_area that takes the parameters x_0, y_0, x_1,y_1, x_2, and y_2 (all numbers), and returns the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). (Hint: use the function point_distance as a helper function and apply Heron's formula.) Triangle area template --- Triangle area solution
"""


import math
def point_distance(x0, y0, x1, y1):
    distance = math.sqrt(((x0 - x1) ** 2) + ((y0 -y1) ** 2))
    return distance

def triangle_area(x0, y0, x1, y1, x2, y2):
    a = point_distance(x0, y0, x1, y1)
    b = point_distance(x2, y2, x1, y1)
    c = point_distance(x0, y0, x2, y2)

    s = (a + b + c) // 2
    area = ((s - a) * (s - b) * (s - c)) ** 0.5
    return area


print("Area of triangle with points (1, 2), (3, 4) and (4, 2): " + str(triangle_area(1, 2, 3, 4, 4, 2)))

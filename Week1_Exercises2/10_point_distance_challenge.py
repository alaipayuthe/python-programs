"""
Challenge: Given the variables x_0, y_0, x_1, and y_1, write an assignment statement that defines a variable distance whose values is the distance between the points (x0,y0) and (x1,y1).
"""

point_x0 = 5
point_y0 = 3

point_x1 = 8
point_y1 = 7

delta_x  = (point_x0 - point_x1) ** 2

delta_y  = (point_y0 - point_y1) ** 2

distance = (delta_x + delta_y) ** 0.5

print("Distance between points: " + str(distance))

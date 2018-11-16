"""
Challenge:Heron's formula states the area of a triangle is sqrt(s(s−a)(s−b)(s−c)) where a, b and c are the lengths of the sides of the triangle and s = 0.5(a + b + c) is the semi-perimeterof the triangle. Given the variables x_0, y_0, x_1, y_1, x_2, and y_2, write a Python program that computes a variable area whose value is the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). (Hint: our solution uses five assignment statements.)
"""

point_x0 = 5
point_y0 = 3

point_x1 = 8
point_y1 = 7

delta_x  = (point_x0 - point_x1) ** 2

delta_y  = (point_y0 - point_y1) ** 2

distance1 = (delta_x + delta_y) ** 0.5

point_x2 = 8
point_y2 = 3

delta_x  = (point_x1 - point_x2) ** 2

delta_y  = (point_y1 - point_y2) ** 2

distance2 = (delta_x + delta_y) ** 0.5

delta_x  = (point_x0 - point_x2) ** 2

delta_y  = (point_y0 - point_y2) ** 2

distance3 = (delta_x + delta_y) ** 0.5

semi_perimeter = (0.5 * (distance1 + distance2 + distance3))

area = (semi_perimeter * ((semi_perimeter - distance1) * (semi_perimeter - distance2) * (semi_perimeter - distance3))) ** 0.5

print("The area of triangle : " + str(area))


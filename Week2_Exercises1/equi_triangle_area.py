"""
Area of equilateral triangle = sqrt(3)/4 * a^2
"""

def equi_triangle_area(a):
    return ((3 ** 0.5) / 4) * (a ** 2)

print("Area with length 2: " + str(equi_triangle_area(2)))

print("Area with length 5: " + str(equi_triangle_area(5)))


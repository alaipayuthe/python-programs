"""
Write a Python function rectangle_perimeter that takes two parameters width and height corresponding to the lengths of the sides of a rectangle and returns the perimeter of the rectangle in inches. Perimeter of rectangle template --- Perimeter of rectangle solution
"""

def rectangle_perimeter(width, height):
    perimeter = 2 * width * height
    return perimeter

print("Rectangle Perimeter(width 4 inches, height 3 inches): " + str(rectangle_perimeter(4, 3)) + " inches")
print("Rectangle Perimeter(width 5 inches, height 6 inches): " + str(rectangle_perimeter(5, 6)) + " inches")

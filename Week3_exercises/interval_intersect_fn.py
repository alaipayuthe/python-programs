""" Program checks whether intervals intersect """

def interval_intersect(param_a, param_b, param_c, param_d):
    """
    Function which takes 4 parameters - a, b, c, d - as input, 
    tests the interval intersection formula, 
    returns True if intervals intersect and False otherwise.
    Interval intersection formula:
    NOT (B <= X OR Y <= A)
    """

    return not((param_b <= param_c) or (param_d <= param_a))

print("(1,2) & (1,5) " + str(interval_intersect(1, 2, 1, 5)))
print("(1,3) & (1,2) " + str(interval_intersect(1, 3, 1, 2)))
print("(4,2) & (6,5) " + str(interval_intersect(4, 2, 6, 5)))
print("(6,2) & (1,9) " + str(interval_intersect(6, 2, 1, 9)))


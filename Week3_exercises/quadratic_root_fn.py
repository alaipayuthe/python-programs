""" Solution - Compute the smaller root of a quadratic equation. """

def smaller_root(coeff_a, coeff_b, coeff_c):
    """
    Returns the smaller root of a quadratic equation with the
    given coefficients.
    """
    
    discriminant = coeff_b ** 2 - 4 * coeff_a * coeff_c
    if discriminant < 0 or coeff_a == 0:
        print("Error: No real solutions")
        return None
    else:
        discriminant_sqrt = discriminant ** 0.5
        # Choose the positive or negative square root that leads to a smaller root.
        if coeff_a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-coeff_b + smaller) / (2 * coeff_a)

print("The smaller root of 1x^2 + 2x + 3 is: ")
print(str(smaller_root(1, 2, 3)))

print("The smaller root of 2x^2 + 0x - 10 is: ")
print(str(smaller_root(2, 0, -10)))


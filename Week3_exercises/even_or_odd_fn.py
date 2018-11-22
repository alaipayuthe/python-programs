""" This program checks whether a number is even. """

def is_even(number):
    """
    Function which takes number as argument and returns True if number is even
    and False if number is odd.
    """
    # Even numbers are divisible by 2
    return bool(number % 2 == 0)
    
print(is_even(5))
print(is_even(100))

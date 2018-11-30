"""
Compute the largest number in a list
"""

def list_max(numbers):
    """
    Given a list of numbers, return the maximum (largest) number
    in the list
    """
    maximum = 0
    if not numbers:
        print("Empty list")
        return None
    else:
        maximum = numbers[0]
        for item in numbers:
            if maximum < item:
                maximum = item
    return maximum

# Tests
print(list_max([4]))
print(list_max([-3, 4]))
print(list_max([5, 3, 1, 7, -3, -4]))
print(list_max([1, 2, 3, 4, 5]))
print(list_max([]))

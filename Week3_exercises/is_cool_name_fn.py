""" This program checks if the given name is either Joe, John or Stephen and prints the result """

def is_cool(name):
    """
    Function which takes name as input argument and returns True if name is in the cool list
    and returns False, if otherwise.
    """
    return bool((name == "Joe") or (name == "John") or (name == "Stephen"))

print(is_cool("Honey"))
print(is_cool("Joe"))
print(is_cool("Nihar"))
print(is_cool("John"))

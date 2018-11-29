""" Program which checks if number is present in the string and prints it """

def make_int(int_string):
    """ 
    Function which takes a string as input, returns an integer if
    numbers are present, returns -1 otherwise
    """

    if int_string.isdigit():
        integer = int(int_string)
    else:
        integer = -1
    return integer

print(make_int("123"))
print(make_int("123re"))
print(make_int("12323"))
print(make_int("*()_++"))
print(make_int("asdf"))


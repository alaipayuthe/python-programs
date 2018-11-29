""" Program which extracts a substring excluding first and last character in the given string """

def get_middle_string(example_string):
    """
    Function which extracts a substring excluding first and last character in the given string
    and prints it
    """
    if len(example_string) < 2:
        print("Error: Invalid string")
    else:
        print("Middle string is: " + example_string[1 : -1])

get_middle_string("Hello World")
get_middle_string("Hello")
get_middle_string("World")
get_middle_string("Hi World")
get_middle_string("Helloooo")
get_middle_string("Radha Madhava")
get_middle_string("Hi")

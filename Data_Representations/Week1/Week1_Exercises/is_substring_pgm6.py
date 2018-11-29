""" Program to test whether a string is a substring of given string """

def is_substring(example_string, test_string):
    """
    Function which takes two strings as input, finds if one is a substring of another,
    returns True if it is, returns False otherwise
    """

    return test_string in example_string

print(is_substring("Om Srikrishnaya Nama", "krishna"))
print(is_substring("Honey Sukesan", "Sambhu"))




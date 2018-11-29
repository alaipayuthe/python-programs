""" Program to slice two substrings with first three and last three characters in a string """

def slice_threes(example_string):
    """
    Function to slice two substrings with first three and last three characters in a string
    and print it
    """
    if len(example_string) < 3:
        print("Error: Invalid string")
    else:
        print("String1: " + example_string[0:3])
        print("String2: " + example_string[-3:])

slice_threes("Hello World")
slice_threes("Hello Earth")
slice_threes("Hello Sun")
slice_threes("Hello Planet")
slice_threes("Hello India")

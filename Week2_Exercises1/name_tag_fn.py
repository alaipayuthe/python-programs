"""
Write a Python function name_tag that takes as input the parameters first_name and last_name (strings) and returns a string of the form "My name is % %." where the percents are the strings first_name and last_name. Reference the test cases in the provided template for an exact description of the format of the returned string. Name tag template --- Name tag solution
"""

def name_tag(first_name, last_name):
    return "My name is " + first_name + " " + last_name

print(name_tag("Honey", "Sukesan"))

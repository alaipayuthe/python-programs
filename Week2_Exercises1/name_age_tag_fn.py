"""
Write a Python function name_and_age that takes as input the parameters name(a string) and age (a number) and returns a string of the form "% is % years old." where the percents are the string forms of name and age. Reference the test cases in the provided template for an exact description of the format of the returned string. Name and age template --- Name and age solution
"""

def name_and_age(name, age):
    return name + " is " + str(age) + " years old"

print(name_and_age("Honey", 32))

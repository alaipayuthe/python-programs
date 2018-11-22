""" Program which concatenates name and age as a string """

def name_and_age(name, age):
    """
    Function which takes name and age as input, validates age
    and returns concatenated string
    """
    if age < 0:
        return "Error:Invalid age"
    else:
        return name + " is " + str(age) + " years old"

print(name_and_age("Honey", 32))
print(name_and_age("hif", -21))

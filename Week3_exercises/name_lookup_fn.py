""" Program which gets the last name of any instructor """

def name_lookup(first_name):
    """
    Function which takes first_name as argument, returns last_name if it is a valid
    instructor or returns error if not.
    """
    if first_name == "Joe":
        last_name = "Warren"
    elif first_name == "Scott":
        last_name = "Rixner"
    elif first_name == "John":
        last_name = "Greiner"
    elif first_name == "Stephen":
        last_name = "Wong"
    else:
        last_name = "Error: Not an instructor"

    return last_name

print("Last name of Joe is " + name_lookup("Joe"))
print("Last name of Scott is " + name_lookup("Scott"))
print("Last name of John is " + name_lookup("John"))
print("Last name of Stephen is " + name_lookup("Stephen"))
print("Last name of Invalid is " + name_lookup("Invalid"))

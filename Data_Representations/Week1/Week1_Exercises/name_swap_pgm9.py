""" Program that swaps an input string delimited by space """

def name_swap(name_string):
    """
    Function which gets an input string delimited by space, swaps it and returns
    the converted string
    """

    index = name_string.find(" ")
    result = name_string[index+1:] + " " + name_string[:index]
    return result

print(name_swap("Honey Sukesan"))
print(name_swap("Sambhu Dayal"))
print(name_swap("Nihar Dayal"))

""" Program to slice a list """

def first_last_slice(example_list):
    """
    Function which takes list as an input, prints a sliced list with
    first and last element
    """

    print(list((example_list[0], example_list[-1])))


list1 = [1, 2, 3, 4]
first_last_slice(list1)
list1 = [1]
first_last_slice(list1)
list1 = [1, 2, 3, 4, 5, 6]
first_last_slice(list1)


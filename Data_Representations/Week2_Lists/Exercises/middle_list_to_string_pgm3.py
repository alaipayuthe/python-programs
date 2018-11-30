""" Program which produces a string excluding first and last element in a list """

def slice_middle(example_list):
    """
    Function which takes a list as an input, validates it,
    slices it to a string excluding first and last item in the list
    """
    if len(example_list) < 2:
        print("Invalid input list")
    else:
        print("".join(example_list[1:-1]))

LIST_1 = ['a', 'b', 'c', 'd']
slice_middle(LIST_1)

LIST_2 = ['a', 'e', 'i', 'o', 'u']
slice_middle(LIST_2)

LIST_3 = ['1']
slice_middle(LIST_3)

"""
Extend a list with another list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
list2 = [0, 0, 0]
example_list.extend(list2)
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

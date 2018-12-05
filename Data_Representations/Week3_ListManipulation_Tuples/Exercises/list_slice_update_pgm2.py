"""
Update a slice of a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_list.pop(1)
example_list.pop(1)
example_list.insert(1, 0)
example_list.insert(1, 0)
example_list.insert(1, 0)

#Simple code below
#example_list[1 : 3] = [0, 0, 0]

print(example_list)

# Output
#[2, 3, 5, 7, 11, 13]
#[2, 0, 0, 0, 7, 11, 13]

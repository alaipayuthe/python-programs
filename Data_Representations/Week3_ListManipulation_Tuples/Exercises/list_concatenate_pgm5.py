"""
Concatenate one list onto another
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
list2 = [0, 0, 0]
new_list = list(example_list)
new_list.extend(list2)

print(example_list)
print(new_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

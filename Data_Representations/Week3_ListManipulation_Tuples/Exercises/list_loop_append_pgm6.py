"""
Append several item to a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
list2 = [0, 0, 0]
for item in list2:
    example_list.append(item)

print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

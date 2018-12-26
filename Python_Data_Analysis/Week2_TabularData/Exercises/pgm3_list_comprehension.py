"""
Template- Create a list zero_list consisting of 3 zeroes using a list comprehension
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

As a challenge, redo the previous problem using a nested list comprehension
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
"""

# Add code here for a list comprehension
ZERO_LIST = list()
for i in range(3):
    ZERO_LIST.append(0)


# Add code here for nested list comprehension
NESTED_LIST = list(ZERO_LIST)
for i in range(4):
    NESTED_LIST.append(ZERO_LIST)


# Tests
print(ZERO_LIST)
print(NESTED_LIST)

# Output
#[0, 0, 0]
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

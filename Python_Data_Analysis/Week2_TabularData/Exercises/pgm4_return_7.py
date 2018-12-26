"""
Template - Select a specific item in a nested list
"""

# Define a nested list of lists
NESTED_LIST = [[col + 3 * row for col in range(3)] for row in range(5)]
print(NESTED_LIST)

# Add code to print out the item in this nested list with value 7
for row in NESTED_LIST:
    if 7 in row:
        for entry in row:
            if entry == 7:
                print(entry)

# Output
#[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
#7

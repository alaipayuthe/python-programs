"""
Template - Analyze another example of a list reference situation
"""

# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Make a copy of list1
list2 = list(list1)

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)

# Explain what happens to list1 in a comment
# A new list is created to save the copy of list1 as list2.
# Hence both are two different lists. Changing an item in one list 
# don't affect another

"""
Flatten a nested list
"""

def flatten(nested_list):
    """
    Given a list whose items are list, 
    return the list formed by joining all of these lists
    """
    flatten_list = []
    if type(nested_list) is list:
        for item in nested_list:
            if type(item) is list:
                for sub_item in item:
                    flatten_list.append(sub_item)
            else:
                flatten_list.append(item)
    return flatten_list

# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]

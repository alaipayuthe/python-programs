"""
Remove duplicates from a list while preserving the order of items
"""

def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """
    clean_list = []
    for item in items:
        if item not in clean_list:
            clean_list.append(item)
    return clean_list

# Test code
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))


# Output
#[]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5, 6]
#['cat', 'dog', 'pig', 'cow', 'pug']

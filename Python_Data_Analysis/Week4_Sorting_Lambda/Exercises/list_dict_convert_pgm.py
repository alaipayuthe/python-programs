""" Exercise program to convert dictionaries to list and vice versa """

def convert_list2dict(gpalist):
    """
    Input: gpalist - list of (student name, gpa) tuples
    Output: a dictionary mapping student names to their gpa
    """
    result = {}
    # Iterate through list, convert list to dict
    for item in gpalist:
        result[item[0]] = item[1]
    return result

def convert_dict2list(gpadict):
    """
    Input: a dictionary mapping student names to their gpa
    Output: gpalist - list of (student name, gpa) tuples
    """
    # Iterate through dict and convert it to list of tuples
    result = []
    keys = gpadict.keys()
    values = gpadict.values()
    tup = tuple(map(lambda num1, num2: (num1, num2), keys, values))
    result.append(tup)

    return result


print(convert_dict2list({"TamikaBarker":3.9, "ElmerBrasher":2.8, "RaymondHathaway":3.3,
                         "RebekahBailey":3.5}))
print(convert_list2dict([("TamikaBarker", 3.9), ("ElmerBrasher", 2.8), ("RaymondHathaway", 3.3),
                         ("RebekahBailey", 3.5)]))

""" This program checks if the given time is lunch time or not """

def is_lunchtime(hour, is_am):
    """
    Function which takes hour and bool argument and returns True if given time is 11am or 12pm
    False otherwise.
    """
    if hour == 11 and (is_am):
        hour_test = True
    elif hour == 12 and (is_am):
        hour_test = True
    else:
        hour_test = False

    return hour_test

print(is_lunchtime(5, True))
print(is_lunchtime(10, True))
print(is_lunchtime(11, False))
print(is_lunchtime(11, True))
print(is_lunchtime(12, False))

""" Program to check given year is leap year or not """

def is_leap_year(year):
    """
    Function which takes year as an input, tests if it's a leap year
    and returns True and False if it is not.
    """

    # Pseudocode from wiki
    # if (year is not divisible by 4) then (it is a common year)
    # else if (year is not divisible by 100) then (it is a leap year)
    # else if (year is not divisible by 400) then (it is a common year)
    # else (it is a leap year)

    if year % 4 != 0:
        leap = False
    elif year % 100 != 0:
        leap = True
    elif year % 400 != 0:
        leap = False
    else:
        leap = True

    return leap

print("Year 2000 : " + str(is_leap_year(2000)))
print("Year 2010 : " + str(is_leap_year(2010)))
print("Year 2018 : " + str(is_leap_year(2018)))
print("Year 1986 : " + str(is_leap_year(1986)))

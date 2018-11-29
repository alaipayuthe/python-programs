"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    
    # Assuming argument validation already happened before this function call.
    date1 = datetime.date(year, month, 1)
    if month < 12:
        date2 = datetime.date(year, month + 1, 1)
    else:
        date2 = datetime.date(year + 1, 1, 1)
    
    # Subtract the first of the given month from the first of the next month
    # to get number of days in that month.
    days = (date2 - date1).days
    
    return days

#print(days_in_month(2018, 12))
#print(days_in_month(2017, 1))
#print(days_in_month(2000, 4))
#print(days_in_month(1986, 4))
#print(days_in_month(2020, 2))
#print(days_in_month(2024, 2))
#print(days_in_month(2016, 2))
#print(days_in_month(2015, 2))


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    # Valid year should be datetime.MINYEAR <= year <= datetime.MAXYEAR
    if (year > datetime.MAXYEAR) or (year < datetime.MINYEAR):
        valid = False
    # Valid month should be 1 <= month <= 12
    elif (month < 1) or (month > 12):
        valid = False
    # Valid day should be 1 <= day <= number of days in the given month and year
    elif (day > days_in_month(year, month)) or (day <= 0):
        valid = False
    else:
        valid = True
        
    return valid

#print(is_valid_date(2000, 2, 12))
#print(is_valid_date(8000, 2, 12))
#print(is_valid_date(2000, 2, 23))
#print(is_valid_date(2018, 42, 12))
#print(is_valid_date(1986, 4, 25))


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    valid = True
    
    # Check validity of the dates
    if is_valid_date(year1, month1, day1):
        date1 = datetime.date(year1, month1, day1)
    else:
        valid = False
    
    if valid:
        if is_valid_date(year2, month2, day2):
            date2 = datetime.date(year2, month2, day2)
        else:
            valid = False
    
    if valid:
        # If dates are valid and first date is earlier than second date,
        # return days between the dates, otherwise return zero.
        if date1 < date2:
            days = (date2 - date1).days
        else:
            days = 0
    else:
        return 0
            
    return days

#print(days_between(2009, 9, 6, 2018, 11, 28))
#print(days_between(2011, 1, 21, 2018, 11, 28))
#print(days_between(1986, 4, 25, 2018, 11, 28))
#print(days_between(2009, 9, 6, 2007, 6, 11))
#print(days_between(2007, 6, 11, 2018, 8, 17))
#print(days_between(-1, 9, 6, 2018, 11, 28))

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    # Check if input date is valid
    if is_valid_date(year, month, day):
        # Find the age in days with respect to today's date
        age = days_between(year, month, day,
                           datetime.date.today().year, 
                           datetime.date.today().month, 
                           datetime.date.today().day)
    else:
        return 0

    return age

#print(age_in_days(1986, 4, 25))
#print(age_in_days(1981, 10, 29))
#print(age_in_days(2011, 1, 21))
#print(age_in_days(2017, 12, 8))
#print(age_in_days(2021, 11, 15))
#print(age_in_days(1963, 6, 30))

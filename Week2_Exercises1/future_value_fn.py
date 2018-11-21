"""
Write a Python function future_value that takes three parameters present_value, annual_rate and years and returns the future value of present_value dollars invested at annual_rate percent interest, compounded annually for years. Future value template --- Future value solution
p(1+0.01r)^y
"""

def future_value(present_value, annual_rate, years):
    value = present_value * ((1 + (0.01 * annual_rate)) ** years)
    return value

print("150 dollars = " + str(future_value(150, 10, 2)))

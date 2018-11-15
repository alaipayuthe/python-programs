"""
Given p dollars, the future value of this money when compounded yearly at a rate of r percent interest for y years is p(1+0.01r)^y. (Remember that you don't need to understand how this formula works, only how to translate it into Python.) Write a Python statement that calculates and prints the value of 1000 dollars compounded at 7 percent interest for 10 years.
"""

# Calculate future value of dollar
print("Future value of dollar = " + str((1000 * ((1 + (0.01 * 7)) ** 10))))


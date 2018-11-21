"""
Challenge: Write a Python function print_digits that takes an integer number in the range [0,100), (i.e., at least 0, but less than 100) and prints the message "The tens digit is %, and the ones digit is %.", where the percent signs should be replaced with the appropriate values. (Hint: Use the arithmetic operators for integer division // and remainder % to find the two digits. Note that this function should print the desired message, rather than returning it as a string. Print digits template --- Print digits solution
"""

def print_digits(number):
    tens  = number // 10
    units = number % 10
    print("Digits in number " + str(number) + " are : " + str(tens) + " and " + str(units))

print_digits(99)
print_digits(32)
print_digits(45)

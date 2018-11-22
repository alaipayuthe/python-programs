""" Program which prints digits in a two digit number """

def print_digits(number):
    """
    Function which takes a number as input, validates it, prints the digits in the number
    """
    if (number < 0) or (number >= 100):
        print("Error: Input is not a two-digit number.")
    else:
        tens = number // 10
        units = number % 10
        print("Digits in number " + str(number) + " are : " + str(tens) + " and " + str(units))

print_digits(99)
print_digits(32)
print_digits(145)
print_digits(45)
print_digits(450)

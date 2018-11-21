"""
Challenge:Powerball is lottery game in which 6 numbers are drawn at random. Players can purchase a lottery ticket with a specific number combination and, if the number on the ticket matches the numbers generated in a random drawing, the player wins a massive jackpot. Write a Python function powerball that takes no arguments and prints the message "Today's numbers are %, %, %, %, and %. The Powerball number is %. The first five numbers should be random integers in the range [1,60), i.e., at least 1, but less than 60. In reality, these five numbers must all be distinct, but for this problem, we will allow duplicates. The Powerball number is a random integer in the range [1,36), i.e., at least 1 but less than 36. Note that this function should print the desired message, rather than returning it as a string. Powerball template --- Powerball solution
"""

import random

def first_five():
    return random.randrange(1, 60)

def powerball_number():
    return random.randrange(1, 36)

def powerball():
    print("Today's numbers are " + str(first_five()) + ", " + str(first_five()) + ", " + str(first_five()) + ", " + str(first_five()) + " and " + str(first_five()) + ".")
    print("The powerball number is " + str(powerball_number()))

powerball()

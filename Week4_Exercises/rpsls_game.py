"""
Week 4 practice project template for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
    
def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4 
    corresponding to numbering in video
    """
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        number = -1
    
    return number
          
def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        name = "rock" 
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"  
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = "Unknown name"
    
    return name
        
def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    
    # print a blank line to separate consecutive games
    print("\n")
    
    # print out the message for the player's choice
    print("Player chooses " + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    if player_number == -1:
        print("Invalid player choice")
        return
        
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    print("Comp_Num: " + str(comp_number))

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
        
    # print out message for computer's choice
    print("Computer chooses " + comp_choice)

    # compute difference of player_number and comp_number modulo five
    modulo = (player_number - comp_number) % 5

    # use if/elif/else to determine winner and print winner message
    if modulo == 0:
        print("Player and computer tie!")
    elif (modulo == 1) or (modulo == 2):
        print("Player wins!")
    elif (modulo == 3) or (modulo == 4):
        print("Computer wins!")
    else:
        print("Invalid option")   
        
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

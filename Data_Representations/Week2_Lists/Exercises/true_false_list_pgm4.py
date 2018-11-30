""" 
Program to create a list of length 16 with first 8 entries as 
True and last 8 entries as False
"""

def create_true_false_list():
    """
    Function which creates and prints a true false list
    """
    sentence = "true " * 8
    sentence = sentence + "false " * 7 + "false"
    print(sentence.split(" "))

create_true_false_list()

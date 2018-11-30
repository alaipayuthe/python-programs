""" Program to split a text sentence into a list """

def text_split_to_list(text):
    """
    Function which takes text STRING as an argument, splits it using " " as delimiter,
    and prints it
    """

    print(text.split())

STRING = "Thequick brownfox jumpsover thelazy dog"
text_split_to_list(STRING)
STRING = "The quick brown fox jumps over the lazy dog"
text_split_to_list(STRING)
STRING = "Thequickbrownfoxjumpsoverthelazydog"
text_split_to_list(STRING)

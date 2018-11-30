""" Program which counts the occurrance of a word in a text string """

def word_count(text, word):
    """
    Function which takes a text string as an input, splits into a list of words,
    counts the occurrance of the given word and prints it
    """
    print(text.split())
    print("No: of occurance of the word " + word + " is " + str((text.split()).count(word)))

word_count("The the the the", "the")
word_count("Mary had a little lamb", "lamb")
word_count("Mary had a little lamb", "lamp")

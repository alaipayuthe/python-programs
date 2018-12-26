""" Program which finds the most occurring letter in a list of words """
def count_letters(word_list):
    """
    Function which takes a list of words as input, count letters in the list
    and return the most occurring letter
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Initialize the letter_count dict
    letter_count = {}
    for letter in alphabet:
        letter_count[letter] = 0
    # Iterate through the word list
    for word in word_list:
        for letter in word:
            letter_count[letter] += 1

    max_value = 0
    max_key = 0
    # Iterate through the letter_count list to find the key with largest value
    for (key, value) in letter_count.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

print(count_letters(["hello", "world"]))

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")
print(count_letters(monty_words))

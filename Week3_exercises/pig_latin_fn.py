""" Program which implements the pig latin game """

def pig_latin(word):
    """
    Function which takes word as input, manipulates the word according to PigLatin game rule,
    and returns the updated string
    """

    if ((word[0] == 'a')
          or (word[0] == 'e')
          or (word[0] == 'i')
          or (word[0] == 'o')
          or (word[0] == 'u')):
        return word + "way"
    elif ((word[0] == 'b')
          or (word[0] == 'c')
          or (word[0] == 'd')
          or (word[0] == 'f')
          or (word[0] == 'g')
          or (word[0] == 'h')
          or (word[0] == 'j')
          or (word[0] == 'k')
          or (word[0] == 'l')
          or (word[0] == 'm')
          or (word[0] == 'n')
          or (word[0] == 'p')
          or (word[0] == 'q')
          or (word[0] == 'r')
          or (word[0] == 's')
          or (word[0] == 't')
          or (word[0] == 'v')
          or (word[0] == 'w')
          or (word[0] == 'x')
          or (word[0] == 'y')
          or (word[0] == 'z')):
        first_letter = word[0]
        rest_string = word[1: ]
        return rest_string + str(first_letter) + "ay"
    else:
        return "Error: Invalid string"

print(pig_latin("apple"))
print(pig_latin("dog"))
print(pig_latin("cat"))
print(pig_latin("egg"))
print(pig_latin("123"))


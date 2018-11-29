def count_vowels(word):
    count = word.count("a")
    count = count + word.count("e")
    count = count + word.count("i")
    count = count + word.count("o")
    count = count + word.count("u")
    return count

print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
    

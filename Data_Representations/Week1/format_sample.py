country = "France"
capital = "Paris"
sentence = "The capital of {} is {}.".format(country, capital)
print(sentence)

mood1 = "happy"
mood2 = "sad"
sentence1 = "I feel {0}, do you feel {0}?  Or are you {1}? I'm not sure if we should be {0}.".format(mood1, mood2)
print(sentence1)

name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)

num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)

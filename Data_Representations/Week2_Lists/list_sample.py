sample = [1, 2, 3]
print(sample)

empty = []
print(empty)

list1 = list()
print(list1)

seq = range(5)
list2 = list(seq)
print(list2)

seq = range(5, 10)
list3 = list(seq)
print(list3)

seq = range(5, 50, 5)
list4 = list(seq)
print(list4)

#List indexing
print(list4[0])
print(list4[2])

# negative indices
print(list4[-1])

#length of the list
print("List length: " + str(len(list4)))

#Out of bounds
#print(list4[25])
#print(list4[-25])

#List slicing
print(list4[1:3])
print(list4[-6:-3])
print(list4[3:])
print(list4[:3])

#invalid indices in list slicing gives empty list 
print(list4[-25:-24])

lst1 = [1, 5, 9, -32]
print(lst1)

lst2 = ["dog", "cow", "horse"]
print(lst2)

emptylst = []
print(emptylst)

lst = list(range(10))

# First element
print(lst[0])

# Third element
print(lst[2])

# Length
print(len(lst))

# Last element
print(lst[9])
print(lst[len(lst) - 1])
print(lst[-1])

lst = list(range(10))

# Slice with 3 elements
print(lst[4:7])

# Slice with the last 2 elements of the list
print(lst[8:10])
print(lst[8:])
print(lst[-2:])

# Slice with the first 4 elements of the list
print(lst[0:4])
print(lst[:4])

# Empty slices
print(lst[20:25])
print(lst[7:3])

items = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(items.index('The'))

#print(items.index('baby'))

print("The" in items)
print("baby" in items)
print("The" not in items)
print("baby" in items)
#Counting item in list
print(items.count("The"))

print(items.count("baby"))

#List iteration
pets = ["cat", "dog", "ferret"]
for animal in pets:
    print(animal)

numbers = [3, 8, -2, 4, 13]
sumsq = 0

for num in numbers:
    square = num * num
    sumsq += square
    
print(sumsq)

length = len(numbers)
for index in range(length):
    print(numbers[index])

# Exercise2 - training.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

num = input("Please enter a number: ")
for item in a:
    if item < num:
        print item
        b.append(item)
print "The new list is:  ", b

# one line only:
b = []
b = [item for item in a if item < num]
print "The new list is:  ", b

# Exercise4 - training.



import random

a = list()
b = list()

a_len = random.choice(range(100))
b_len = random.choice(range(100))

print a_len
print b_len

a = [random.randrange(10) for i in range(a_len)]
b = [random.randrange(10) for i in range(b_len)]

print "Original list - A = ", a
print "Original list - B = ", b

c = list()

# without repetition:
c = list(set([a_item for a_item in a for b_item in b if a_item == b_item]))

print "New list - C = ", c


'''
General "how-to" guide (internal use for me !)
# note - when using sample - we do not allow duplicates !
#a = random.sample(range(100), a_len)
#b = random.sample(range(100), b_len)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# with repetition:
c = [a_item
     for a_item in a
        for b_item in b
            if a_item == b_item]
print a
print b
print c

# without repetition
for a_item in a:
    for b_item in b:
        if a_item == b_item:
            for c_item in c:
                if c_item == a_item:
                    c.remove(a_item)
            c.append(a_item)
            print "a=",a_item,"b=",b_item
print a
print b
print c
'''



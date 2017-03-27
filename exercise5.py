# Exercise5 - training.

'''
Fibonacci numbers:
Fn+1 = Fn+Fn-1
'''

# NOTE - Fibonacci numbers can appear with F1=F2=1 or F1=0,F2=1,
#       to change the program to support F1=F2=1 we need to
#       change the condition to if(num==1 or num==2) - return 1

from array import *

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1

    return fib(num-1) + fib(num-2)


num = input("Please enter a number: ")

a = array('i',[0,1])
for i in range(num-2):
    a.append(a[i+1] + a[i])
print "[array] The Fibonacci sequence for f(",num,") is:"
print a.tolist()



num = input("Please enter a number: ")
print "[recursive] The Fibonacci number for f(",num,") is", fib(num)

print "[recursive] The Fibonacci sequence for f(",num,") is:"
for i in range(num):
    print fib(i)



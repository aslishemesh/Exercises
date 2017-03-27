# Exercise4 - training.

'''
Fibonacci numbers:
Fn+1 = Fn+Fn-1
'''

# NOTE - Fibonacci numbers can appear with F1=F2=1 or F1=0,F2=1,
#       to change the program to support F1=F2=1 we need to
#       change the condition to if(num==1 or num==2) - return 1

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a = fib(num-1) + fib(num-2)
        return a

num = input("Please enter a number: ")

for i in range(num):
    print fib(i)



# Exercise1 - training.


def check_div_even(num, check):
    if num % check == 0:
        return True
    else:
        return False


num = input("Please enter a number: ")

#if check_div_even(num,4) == True:
if check_div_even(num, 4):
        print "The number %d can be divided by 4" % num
#elif check_div_even(num, 2) == True:
elif check_div_even(num, 2):
    print "The number %d is an even number but not a multiple of 4" % num
else:
    print "The number %d is an odd number and therefor cannot be divided by 2 or 4" % num

check = input("please enter a number to check (as a divider): ")

#if check_div_even(num,check) == True:
if check_div_even(num, check):
        print "The number %d can be divided by %d" % (num, check)
else:
    print "The number %d cannot be divided by %d" % (num, check)
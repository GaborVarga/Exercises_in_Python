#!/usr/bin/env python

#######################
# Author: Gabor Varga #
#######################

# Exercise No. 2
# Description :
# 
# Define a function max_of_three() that takes three numbers 
# as arguments and returns the largest of them.
#
# http://www.ling.gu.se/~lager/python_exercises.html

import sys
from pip._vendor.distlib.compat import raw_input

###############
# Function(s) #
###############

def maxi(numbers):    
    m = -1
    ii = 0
    for i in range (len(numbers)):
        if m < numbers[i]:
            m = numbers[i]
            ii = i
    ii = ii + 1
    print("The largest number's index is:",ii)
    print("The largest number is:",m)
    
##########            
# Script #
##########

okay = 0
while okay != 1 :
    try :
        number1 = int(raw_input("Please enter the first number: \n"))
        okay = okay + 1
    except ValueError :
        print("Sorry but this is not a number.\n")
        okay = 0
        continue
okay = 0
while okay != 1 :
    try :
        number2 = int(raw_input("Please enter the second number: \n"))
        okay = okay + 1
    except ValueError :
        print("Sorry but this is not a number.\n")
        okay = 0
        continue
okay = 0
while okay != 1 :
    try :
        number3 = int(raw_input("Please enter the third number: \n"))
        okay = okay + 1
    except ValueError :
        print("Sorry but this is not a number.\n")
        okay = 0
        continue
    
nums = [number1,number2,number3]
maxi(nums)
    
sys.exit()
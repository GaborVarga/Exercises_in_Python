#!/usr/bin/env python

#######################
# Author: Gabor Varga #
#######################

# Exercise description :
# 
# Define a function maxi() that takes two numbers as arguments and returns 
# the largest of them. Use the if-then-else construct available in Python. 

# 
# http://www.ling.gu.se/~lager/python_exercises.html

import sys
from pip._vendor.distlib.compat import raw_input

###############
# Function(s) #
###############
def maxi(n1, n2):
    if n1 > n2:
        print("The largest is",n1,"!")
    else :
        if n1 == n2 :
            print("The numbers are equal.")
        else :
            print("The largest is",n2,"!")

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
        number2 = int(raw_input("Please enter another number: \n"))
        okay = okay + 1
    except ValueError :
        print("Sorry but this is not a number.\n")
        okay = 0
        continue

maxi(number1, number2)

sys.exit()
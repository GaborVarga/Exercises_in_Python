#!/usr/bin/env python

#######################
# Author: Gabor Varga #
#######################

# Exercise description :
# 
# Write a function that takes a character (i.e. a string of length 1) 
# and returns True if it is a vowel, False otherwise.
# 
# http://www.ling.gu.se/~lager/python_exercises.html

from pip._vendor.distlib.compat import raw_input

###############
# Function(s) #
###############

def checkchar (c):
    vowels = ['a','e','i','o','u']
    if c in vowels:
        print("\nThis is a vowel!")
        return True
    else :
        print("This is not a vowel.")
        return False

##########            
# Script #
##########

singlechar = raw_input("Please type 1 character: ")

while len(singlechar) != 1 :
    singlechar = raw_input("Please type only 1 character: ")

print(checkchar(singlechar))

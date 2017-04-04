#!/usr/bin/env python

#######################
# Author: Gabor Varga #
#######################

# Exercise description :
# Define a function is_palindrome() that recognizes palindromes 
# (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.
# 
# http://www.ling.gu.se/~lager/python_exercises.html

###########
# imports #
###########

from pip._vendor.distlib.compat import raw_input
from builtins import int

###############
# Function(s) #
###############

def ispalindrome(inputstring) :
    if(len(inputstring)%2==0):
        return inputstring[:int(len(inputstring)/2)] == \
            reverse(inputstring[int(len(inputstring)/2):])
    else :
        return inputstring[:int((len(inputstring)-1)/2)]== \
            reverse(inputstring[int(((int(len(inputstring))-1)/2)*-1):])
    
def reverse(inputstring):
    result = "" 
    for karakter in inputstring:
        result = karakter + result
    return result

##########            
# Script #
##########

inputstring = raw_input("Please enter a string: \n")
print("Is it a plaindrome? ",ispalindrome(inputstring))
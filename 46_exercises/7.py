#!/usr/bin/env python

#######################
# Author: Gabor Varga #
#######################

# Exercise description :
# 
# Define a function reverse() that computes the reversal of a string. 
# For example, reverse("I am testing") should return the string "gnitset ma I".
# 
# http://www.ling.gu.se/~lager/python_exercises.html

###########
# imports #
###########

from pip._vendor.distlib.compat import raw_input

###############
# Function(s) #
###############

def reverse(inputstring):
    result = "" 
    for karakter in inputstring:
        result = karakter + result
    return result

##########            
# Script #
##########

inputstring = raw_input("Please enter a string: \n")
print("The reverse string is: ",reverse(inputstring))
#!/usr/bin/env python

#######################
# Author: Gabor Varga #
#######################

# Exercise description :
# 
# Define a function that computes the length of a given list or string. 
# (It is true that Python has the len() function built in, but writing it 
# yourself is nevertheless a good exercise.)
# 
# http://www.ling.gu.se/~lager/python_exercises.html

import sys
from pip._vendor.distlib.compat import raw_input

###############
# Function(s) #
###############


##########            
# Script #
##########


inputstring = raw_input("Please enter a string to determine its length: \n")

i = 0
for character in inputstring :
    i = i +1
    # print (character)
print ("\nLength of the given string is: ",i)
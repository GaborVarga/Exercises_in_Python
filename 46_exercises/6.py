#!/usr/bin/env python

#######################
# Author: Gabor Varga #
#######################

# Exercise description :
# 
# Define a function sum() and a function multiply() that sums and multiplies 
# (respectively) all the numbers in a list of numbers. 
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) 
# should return 24.
# 
# http://www.ling.gu.se/~lager/python_exercises.html

###########
# imports #
###########

###############
# Function(s) #
###############

def summarise (array):
    summa = 0
    for i in array:
        summa = summa + i
    return summa

def multiply (array):
    multi = 1
    for i in array:
        multi = multi * i
    return multi

##########            
# Script #
##########

myarray = [1,2,3,4,5,6,7,8,9,10]

res = summarise(myarray)
print("Sum of numbers from 1 to 10: ",res)

res = multiply(myarray)
print("\nMultiplication of numbers from 1 to 10: ",res)
#!/usr/bin/env python

#######################
# Author: Gabor Varga #
#######################

# Exercise description :
# 
# Write a function translate that will translate a text into "roovarspraaket"
# (Swedish for "robber's language"). That is, double every consonant 
# and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string 
# "tothohisos isos fofunon".
# 
# http://www.ling.gu.se/~lager/python_exercises.html

###########
# Imports #
###########

from pip._vendor.distlib.compat import raw_input

###############
# Function(s) #
###############

def translate(instr):
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s',
                 't','v','z','x','y','w']
    res = ""
    for c in instr :
        if c in consonants :
            res = res + c + "o" + c
        else :
            res = res + c
    return res

##########            
# Script #
##########

inputstring = raw_input("Please type a string and I will translate it to robber language: ")

while len(inputstring) == 0 :
    inputstring = raw_input("Please type a string: ")

print("\nThe input string in robber language : ")
print(translate(inputstring))
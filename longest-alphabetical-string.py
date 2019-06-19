#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:06:40 2019

@author: AndrewKim
"""

alphabet = []
for letters in range(97, 123):
    alphabet.append(chr(letters))
    
number = 0

longestString = ""
tempLongestString = ""
index = 0

for i in s:
    if (len(longestString) == 0):
        longestString += i
        currentIndex = alphabet.index(i)
        index = currentIndex
    elif (len(longestString) != 0):
        currentIndex = alphabet.index(i)
        if (currentIndex >= index):
            longestString += i
            index = currentIndex
        elif (currentIndex < index) and (len(longestString) > len(tempLongestString)):
            tempLongestString = longestString
            longestString = ""
            longestString += i
            index = currentIndex
        elif (currentIndex < index) and (len(longestString) <= len(tempLongestString)):
            longestString = ""
            longestString += i
            index = currentIndex
            
        
if (len(longestString) > len(tempLongestString)):
    print("Longest substring in alphabetical order is: " + str(longestString))
else:
    print("Longest substring in alphabetical order is: " + str(tempLongestString))
    
        
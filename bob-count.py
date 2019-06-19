#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:34:37 2019

@author: AndrewKim
"""

number = 0
store = ""

for i in s:
    if (len(store) == 0) and (i == "b"):
        store += i
    elif(len(store) == 1) and (i == "o"):
        store += i
    elif(len(store) == 1) and (i == "b"):
        continue
    elif(len(store) == 2) and (i == "b"):
        number += 1
        store = ""
        store += i
    else:
        store = ""

print("Number of times bob occurs is: " + str(number))
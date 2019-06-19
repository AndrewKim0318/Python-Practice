#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:29:47 2019

@author: AndrewKim
"""

vowels = 0
s = 'azcbobobegghakl'

for i in s:
    if (i == "a") or (i =="e") or (i == "i") or (i == "o") or (i == "u"):
        vowels += 1

print("Number of vowels: "+ str(vowels))
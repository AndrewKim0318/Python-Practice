#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:54:32 2019

@author: AndrewKim
"""

print("Please think of a number between 0 and 100!")

low = 0
high = 100
guessed = False

while not guessed:
    answer = (low + high) // 2
    print("Is your secret number " + str(answer))
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if hint == "c":
        guessed = True
    elif hint =="h":
        high = answer
    elif hint == "l":
        low = answer
    else:
        print("Sorry, I did not understand your input")

print("Game over. Your secret number was: " + str(answer))
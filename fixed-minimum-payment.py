#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:03:14 2019

@author: AndrewKim
"""
balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12

def minimumPayment(lowerBound, upperBound):
    
    monthlyPayment = (lowerBound + upperBound)/2
    previousBalance = balance
    month = 0
    
    while month < 12:
        month += 1
        monthlyUnpaidBalance = previousBalance - monthlyPayment
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        previousBalance = updatedBalance
    
    guessed = False
    while guessed == False:
        if updatedBalance <= 0.01 and updatedBalance >= -0.01:
            guessed = True
            lowestPayment = round(monthlyPayment, 2)
            print("Lowest Payment: " + str(lowestPayment))
            return monthlyPayment
        elif updatedBalance < -0.01:
            upperBound = monthlyPayment
            return minimumPayment(lowerBound, upperBound)
        elif updatedBalance > 0.01:
            lowerBound = monthlyPayment
            return minimumPayment(lowerBound, upperBound)

x= balance/12
y= (balance * (1 + monthlyInterestRate)**12)/12.0
minimumPayment(x, y)


        
        
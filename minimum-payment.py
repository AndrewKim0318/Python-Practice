#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:46:11 2019

@author: AndrewKim
"""
import math

balance = 4773
annualInterestRate = 0.2

month = 0
minimumFixedMonthlyPayment = balance/12
previousBalance = balance

while month < 12:
    month += 1
    monthlyInterestRate = annualInterestRate/12.0
    monthlyUnpaidBalance = previousBalance - minimumFixedMonthlyPayment
    updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    previousBalance = updatedBalance
    minimumFixedMonthlyPayment += (monthlyInterestRate * monthlyUnpaidBalance)/12
    
def roundup(x):
    return int(math.ceil(x/10) *10)

lowestPayment = roundup(minimumFixedMonthlyPayment)
print("Lowest Payment: " + str(lowestPayment))
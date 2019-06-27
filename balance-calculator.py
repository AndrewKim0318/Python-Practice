#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:30:59 2019

@author: AndrewKim
"""

month = 0
monthlyBalance = balance

while month < 12:
    month += 1
    previousBalance = monthlyBalance
    monthlyInterestRate = annualInterestRate/12.0
    minimumMonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
    monthlyBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

remainingBalance = round(monthlyBalance, 2)
print("Remaining balance: " + str(remainingBalance))
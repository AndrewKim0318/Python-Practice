#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:26:54 2019

@author: AndrewKim
"""

def gcdRecur(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    elif a%b ==0:
        return a
    else:
        return gcdRecur(b,a%b)

gcdRecur(2,0)
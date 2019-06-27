#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:55:40 2019

@author: AndrewKim
"""

import math

def polysum(n,s):
    """
    input n, a positive int, declaring number of side
    input s, a positive int or float, declaring length of side
    returns the sum of the area + square of perimeter of a given polymer
    """
    area = (0.25 * n * s**2) / (math.tan(math.pi/n))
    perimeter = s * n
    
    sum = round((area + perimeter**2),4)
    return sum

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:25:13 2021

@author: shumka
"""
N = 5;
factorial = 1

def squirrel(N):
    while N > 1:
        factorial *= N
        N -= 1
factorial = str(factorial)
emerald_nuts = factorial[0]
return emerald_nuts
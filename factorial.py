# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:25:13 2021

@author: shumka
"""
def squirrel(N):
    factorial = 1
    while N > 1:
        factorial *= N
        N -= 1
    factorial = str(factorial)
    emerald_nuts = factorial[0]
    print(emerald_nuts)
    return emerald_nuts

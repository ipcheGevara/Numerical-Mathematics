# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:41:22 2021

@author: lukag
"""

#Formirajte Newtonov interpolacijski polinom koji interpolira funkciju
#f(x) = e**x u cvorovima 2, 3, 5 i ocijenite gresku u tocki 2.1.

from numpy import *
import pylab as pl

x = array([2, 3, 5])

def f(x):
    return e**x
y = f(x)

n = len(x)

def NewtonCoef(x, y):
    a = []
    for i in range(n):
        a.append(y[i])
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i] - a[i-1]) / float(x[i] - x[i-j])
        return a

def Greska(z):
    M = e**z
    omega = 1.0
    for i in range(0, n):
        omega *= (z-x[i])
    return abs(omega) * M/math.factorial(3)

print(x)
print(y)
print('Koeficijenti Newtonovog polinoma:')
print(NewtonCoef(x, y))
print('Ocjena greske za x=2.1: ',Greska(2.1))
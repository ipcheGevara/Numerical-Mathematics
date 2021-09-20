# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:36:14 2021

@author: lukag
"""

#Zadana je funkcija f(x) = sin(x) na segmentu [0, 1].
#Interpolirati zadanu funkciju Newtonovim interpolacijskim polinomom
#koji prolazi tockama x0 = 0, x1 = 0.25, x2 = 0.5, x3 = 0.75, x4 = 1.
#Odrediti uniformnu gresku interpolacije u tocki 0.9.

from numpy import *
import pylab as pl

def f(x):
    return sin(x)

# Formiramo listu ekvidistantnih cvorova
a = 0
b = 1
n = 4
h = (b-a) / n
x = []
for i in range(n+1):
    x.append(a+h*i)
    
y = f(x)

n = len(x)

k = []
for i in range(n):
    k.append(y[i])

for j in range(1, n):
    for i in range(n-1, j-1, -1):
        k[i] = float(k[i] - k[i-1])

a = []
for i in range(n):
    a.append(k[i])
for i in range(1, n):
    a[i] = a[i] / (math.factorial(i)*h**i)
    
print(x)
print(y)
print('Koeficijenti NIP-a:')
print(a)

def Greska(z):
    M5 = cos(z)
    omega = 1.0
    for i in range(0, n):
        omega *= (z-x[i])
    return abs(omega)*M5/math.factorial(5)

print('Newtonov polinom:')
print('P4(x)=',a[0],'+',a[1],'(x-',x[0],')+',a[2],'(x-',x[0],')(x-',x[1],')+',\
       a[3],'(x-',x[0],')(x-',x[1],')(x-',x[2],')+',\
       a[4],'(x-',x[0],')(x-',x[1],')(x-',x[2],')(x-',x[3],')')

print('Ocjena greske za x=0.9: ',Greska(0.9))





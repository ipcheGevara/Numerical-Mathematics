# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:55:48 2021

@author: lukag
"""

#Za zadane podatke odrediti Newtonov interpolacijski polinom P2(x) ako je zadano
#  x  -2  2    4
#f(x) -5  3  211
#Za zadane podatke odrediti Newtonov interpolacijski polinom
#i odrediti njegovu vrijednost za x = 1.

from numpy import *

x = array([-2,2,4])
y = array([-5,3,211])

n = len(x)
a = []
for i in range(n):
    a.append(y[i])

for j in range(1, n):
    for i in range(n-1, j-1, -1):
        a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])
    
print(x)
print(y)
print('Koeficijenti Newtonovog polinoma:')
print(a)
print('Newtonov polinom:')
print('P2(x)=',a[0],'+',a[1],'(x-',x[0],')+',a[2],'(x-',x[0],')(x-',x[1],')')

def vrijednost(a,x,v):
    z = a[0]
    faktor = 1.0
    for i in range(1,n):
        faktor*=(v-x[i-1])
        z+=(a[i]*faktor)
    return z
    
print('P2(1)=',vrijednost(a,x,1))





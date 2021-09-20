# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:22:40 2021

@author: lukag
"""

from numpy import *
from numpy.polynomial import polynomial as p
from numpy import linalg as l
import pylab as pl

def f(x):
    return sin(pi*x)
def df(x):
    return pi * sin(pi*x)

# Definiramo matrice
M1 = array([[1, 0, 0], [1, 1./2, 1./4], [0, 1, 0]])
M2 = array([0, 1, pi])

# Rjesavamo sustav matrica kako bi dobili koeficijente a
a = l.solve(M1, M2)
print('Koeficijenti interpolacijskog polinoma su: ', a)

der = p.polyder(a)
print('Koeficijenti derivacije interpolacijskog polinoma su: ', der)

# Provjera uvjeta
print('Provjera uvjeta interpolacijskog polinoma:')
print('p(0)=', p.polyval(0., a))
print('p(0.5)=', p.polyval(0.5, a))
print('p\'(0)=', p.polyval(0, der))

print('Vrijednost interpolacijskog polinoma za x=0.2:', p.polyval(0.2,a))
print('f(0.2)=', f(0.2))
print('Relativna greska za x=0.2:', abs(p.polyval(0.2,a)-f(0.2))/f(0.2))

x=linspace(0-0.5,0+0.5,100)
y=p.polyval(x,a)
y1=f(x)
pl.plot(x,y,'g-',x,y1,'r-')
pl.grid()
pl.show()


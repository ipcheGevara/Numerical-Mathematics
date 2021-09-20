# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:36:01 2021

@author: lukag
"""

import pylab as pl
import numpy as np
from numpy.polynomial import polynomial as p
from numpy import linalg as l

def f(x):
    return x * np.cos(np.pi*x)



# Definiramo matrice
M1 = np.array([[1, -1, 1], [1, 0, 0], [1, 1, 1]])
M2 = np.array([1, 0, -1])

# Rjesavamo matricni sustav kako bi dobili koeficijente a
a = l.solve(M1, M2)
print(a) # -x

# Provjera uvjeta uvrstavanjem koeficijenata
print('f(1)=', p.polyval(1., a))
print('f(0)=', p.polyval(0., a))
print('f(-1)=', p.polyval(-1., a))

print('Vrijednost interpolacijskog polinoma za x=0.4:', p.polyval(0.4,a))

print('Vrijednost funkcije za x=0.4:', f(0.4))
print('Relativna greska za x=0.4:', abs(p.polyval(0.4,a)-f(0.4))/abs(f(0.4)))

# Crtanje
x=np.linspace(-1-0.5,1+0.5,100)
y = f(x)
g = p.polyval(x, a)
pl.plot(x, y, 'b-', x, g, 'r--')
pl.grid()
pl.show()

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:13:07 2021

@author: lukag
"""


import pylab as pl
import numpy as np
from numpy.polynomial import polynomial as p
from numpy import linalg as l


# Definiramo matrice
M1 = np.array([[1, 0, 0, 0], [1, np.pi, np.pi**2, np.pi**3], [0, 1, 0, 0],[0, 1, 2*np.pi, 3*np.pi**2]])
M2 = np.array([0, 0, 1, -1])

# Rijesavamo sustav jednadzbi kako bi dobili koeficijente a za polinom
a = l.solve(M1, M2)
print(a) # x - 0.32x**2

# Derivacija polinoma
der = p.polyder(a)

# Provjera uvjeta
print('p(0)=', p.polyval(0., a))
print('p(pi)=', p.polyval(np.pi, a))
print('p\'(0)=', p.polyval(0., der))
print('p\'(pi)=', p.polyval(np.pi, der))

# Crtanje 
x = np.linspace(0-0.5, 4, 100)
y = p.polyval(x, a)
z = np.sin(x)

pl.plot(x, y, x, z)
pl.grid()
pl.show()


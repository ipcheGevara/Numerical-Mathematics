# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:54:57 2021

@author: ipcheGevara
"""

import pylab as pl
import numpy as np
from numpy.polynomial import polynomial as p
from numpy import linalg as l

# Definiramo matrice

M1 = np.array([[1,0,0], [1,1,1], [0, 1, 0]])
M2 = np.array([1, 1, 1])

# Rjesavamo matricnu jednadzbu kako bi
# dobili koeficijente a

a = l.solve(M1, M2)
print(a) # 1 + x - x**2

# Derivacija polinoma
d = p.polyder(a)

# Provjera uvjeta
print('p(0)=', p.polyval(0., a))
print('p(1)=', p.polyval(1., a))
print('p\'(0)=', p.polyval(0., d))

# Crtanje dobivenog polinoma
x = np.linspace(0, 5, 100)
y = p.polyval(x, a)
pl.plot(x, y)
pl.grid()
pl.show()



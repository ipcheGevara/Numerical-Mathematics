# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:15:56 2021

@author: ipcheGevara
"""

import pylab as pl
import numpy as np
from numpy.polynomial import polynomial as p
from numpy import linalg as l

# Definiramo matrice
M1 = np.array([[1, 0, 0], [1, 1, 1], [1, 4, 16]])
M2 = np.array([1, 3, 0])

print(M1)
print(M2)

# Rjesavamo matricnu jednadzbu
a = l.solve(M1, M2)
print(a) # 1 + 2.75x - 0.75x**2

# Uvrstavamo x u polinom da provjerimo uvjete
print('p(0)=', p.polyval(0., a))
print('p(1)=', p.polyval(1., a))
print('p(4)=', p.polyval(4., a))

# Crtamo dobiveni interpolacijski polinom
x = np.linspace(-5, 5, 100)
y = p.polyval(x, a)

pl.plot(x, y)
pl.grid()
pl.show()




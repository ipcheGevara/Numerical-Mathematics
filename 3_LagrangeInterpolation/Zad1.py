# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:33:24 2021

@author: ipcheGevara
"""

#Odredite interpolacijski polinom ako su zadani uvjeti:
#p(0) = 3, p(2) = 4, p(4) = 2

import pylab as pl
import numpy as np
from numpy import linalg as l
from numpy.polynomial import polynomial as p

# Definiramo odgovarajuce matrice
M1 = np.array([[1, 0, 0], [1, 2, 4], [1, 4, 6]])
M2 = np.array([3, 4, 2])

#Rjesavamo matricnu jednadbu
a = l.solve(M1, M2) 
print(a)

# Uvrstavamo x u polinom a
print('p(0)=', p.polyval(0., a))
print('p(2)=', p.polyval(2., a))
print('p(4)=', p.polyval(4., a))

x = np.linspace(-0.5, 5, 100)
y = p.polyval(x, a)
pl.plot(x, y)
pl.grid()
pl.show()




# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:43:45 2021

@author: lukag
"""

# Konstruirajte i odredite interpolacijski polinom koji zadovoljava uvjete:
# p(1)=1, p'(1)=2, p(4)=3

import pylab as pl
import numpy as np
from numpy.polynomial import polynomial as p
from numpy import linalg as l

# Definiramo matrice
M1 = np.array([[1, 1, 1], [1, 4, 16], [0, 1, 2]])
M2 = np.array([1, 3, 2])

# Rijesimo sustav matrica da dobijemo koeficijente a
a = l.solve(M1, M2)
print(a) 

# Derivacija polinoma
der = p.polyder(a)

# Provjera uvjeta
print('p(1)=', p.polyval(1., a))
print('p(4)=', p.polyval(4., a))
print('p\'(1)=', p.polyval(1., der))

# Crtanje
x = np.linspace(0-0.5, 5, 100)
y = p.polyval(x, a)

pl.plot(x, y)
pl.grid()
pl.show()


# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:24:29 2021

@author: lukag
"""
# Konstruirajte i odredite interpolacijski polinom koji zadovoljava uvjete:
# p(0)=1, p'(0)=1, p(1)=1

import numpy as np
import pylab as pl
from numpy.polynomial import polynomial as p
from numpy import linalg as l

# Definiramo matrice
M1 = np.array([[1, 0, 0], [1, 1, 1], [0, 1, 0]])
M2 = np.array([1, 1, 1])

# Rijesimo sustav jednadzbi kako bi dobili koeficijente a
a = l.solve(M1, M2)
print(a) # 1 + x - x**2

# Deriviramo polinom
der = p.polyder(a)

# Provjeravamo uvjete
print('p(0)=', p.polyval(0., a))
print('p(1)=', p.polyval(1., a))
print('p\'(0)=', p.polyval(0., der))

# Crtamo dobiveni interpolacijski polinom

x = np.linspace(0, 5, 100)
y = p.polyval(x, a)
pl.plot(x, y)
pl.grid()
pl.show()

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:47:26 2021

@author: lukag
"""

# Na ravnoj podlozi projekti je ispaljen pod kutem od 45 stupnjeva
#i pao je 580 m dalje. Procijenite maksimalnu visinu koju je
#projektil postigao.


from numpy import *
from numpy.polynomial import polynomial as p
import pylab

M1=array([[1,0,0], [0,1,0], [1,580, 580**2]])
M2=array([0,1,0])

print(M1)
print(M2)

a=linalg.solve(M1, M2)
print(a)

print('p(0)=', p.polyval(0.,a))
print('p(580)=', p.polyval(580.,a))

d=p.polyder(a)

print('p\'(0)=', p.polyval(0.,d))

print('Maksimalna visina je: ', p.polyval(580./2, a))

x=linspace(0-0.5, 600, 100)
y=p.polyval(x, a)
pylab.plot(x,y)
pylab.show()
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:37:17 2021

@author: lukag
"""

from numpy import *
import scipy.integrate as spi
from scipy import interpolate as i
import pylab as pl

def f(x):
    return x**2 - x +1

a = 1
b = 3
c = (a+b) / 2

x1 = array([a, b])
x2 = array([a, c, b])
y1 = f(x1)
y2 = f(x2)

iTrap = spi.trapz(y1, x1)
iSimp = spi.simps(y2, x2)

print('Vrijednost trapezne formule je: ', iTrap)
print('Vrijednost simpsonove formule je: ', iSimp)

integral = 3**3 / 3 - 1/3 - 3**2 / 2 + 1/2 + 3 - 1

print('Prava vrijednost integrala je: ', integral)

print('Prava greska trapezne formule je: ', iTrap - integral)
print('Prava greska simpsonove formule je: ', iSimp - integral)

M2 = 2
M4 = 0

apsGrTrap = (((b-a)**3)/12) * M2
apsGrSimp = ((b-a)/2)**5 * (M4/90)

print('Apsolutna greska trapezne formule je: ', apsGrTrap)
print('Apsolutna greska simpsonove formule je: ', apsGrSimp)
print('U ovom slucaju je Simpsonova formula egzaktna')

# kreiramo Lagrangea kako bi nacrtali simpsonovu formulu
pL = i.lagrange(x2, y2)
print('Lagrange: ', pL)

xtocke = linspace(a, b, 100)
ytocke = f(xtocke)
pl.figure()
pl.plot(xtocke, ytocke, x1, y1, xtocke, pL(xtocke), x2, y2)
pl.legend(['funkcija', 'Trapezna formula', 'Lagrange', 'Simpsonova'])
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.grid()
pl.fill_between(xtocke, ytocke)
pl.show()
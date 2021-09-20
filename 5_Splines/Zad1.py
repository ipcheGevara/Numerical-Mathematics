# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 14:59:54 2021

@author: lukag
"""

from numpy import *
from scipy import interpolate
import pylab as pl

def f(x):
    return x**2 * sin(x)

xcvorovi = linspace(-pi, pi, 20)
ycvorovi = f(xcvorovi)

print(xcvorovi)
print(ycvorovi)

# Formiramo linearni spline
lspline = interpolate.interp1d(xcvorovi, ycvorovi, kind = 'slinear')
# Izracunavamo apsolutnu gresku
print('Apsolutna greska u x=1 je: ', abs(lspline(1) - f(1)))

# Definiramo tocke za crtanje
xtocke = linspace(min(xcvorovi), max(xcvorovi), 100)
yspline = lspline(xtocke) #aproksimacija funkcije
yfunkcija = f(xtocke) #egzaktna funkcija

pl.figure()
pl.plot(xcvorovi, ycvorovi, 'o', xtocke, yspline, '--', xtocke, yfunkcija, '-g')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.legend(['cvorovi', 'lspline', 'funkcija'])
pl.grid()
pl.show()


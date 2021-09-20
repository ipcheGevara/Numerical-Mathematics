# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:24:13 2021

@author: lukag
"""

from numpy import *
from scipy import interpolate
import pylab as pl

def f(x):
    return x*sin(x)

# Cvorovi - koristimo ih za definiranje splinea
xcvorovi = genfromtxt('Tocke.txt', delimiter=',')
ycvorovi = f(xcvorovi)

print(xcvorovi)
print(ycvorovi)

lspline = interpolate.interp1d(xcvorovi, ycvorovi, kind='slinear')
kspline = interpolate.interp1d(xcvorovi, ycvorovi, kind='cubic')

apsGrL = abs(f(1) - lspline(1))
apsGrC = abs(f(1) - kspline(1))
relGrL = apsGrL / abs(f(1))
relGrC = apsGrC / abs(f(1))

print('Apsolutna greska u tocki x=1 za lspline: ', apsGrL)
print('Apsolutna greska u tocki x=1 za kspline: ', apsGrC)
print('Relativna greska u tocki x=1 za lspline: ', relGrL)
print('Relativna greska u tocki x=1 za lspline: ', relGrC)

# Definiramo tocke koje su nam potrebne za crtanje
xtocke = linspace(min(xcvorovi), max(xcvorovi), 100)
yfunkcija = f(xtocke) # Egzaktna funkcija
ylspline = lspline(xtocke)
ykspline = kspline(xtocke)

# Crtanje
pl.figure()
pl.plot(xcvorovi, ycvorovi, 'o', xtocke, ylspline, 'r-', xtocke, ykspline, 'b-', xtocke, yfunkcija, '--')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.legend(['cvorovi', 'lspline', 'kspline', 'funkcija'])
pl.grid()
pl.show()




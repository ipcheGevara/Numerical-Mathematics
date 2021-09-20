# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:07:17 2021

@author: lukag
"""

from numpy import *
from scipy import interpolate
import pylab as pl

def f(x):
    return 1. / (1 + 5*x**2)

# Cvorovi
xcvorovi = linspace(-1, 1, 20)
ycvorovi = f(xcvorovi)

kspline = interpolate.interp1d(xcvorovi, ycvorovi, kind='cubic')
apsGr = abs(f(0.95) - kspline(0.95))
relGr = apsGr / abs(f(0.95))

print('Apsolutna greska u tocki x=0.95 iznosi: ', apsGr)
print('Apsolutna greska u tocki x=0.95 iznosi: ', relGr)

# Definiramo tocke za crtanje
xtocke = linspace(min(xcvorovi), max(xcvorovi), 100)
ytocke = f(xtocke) # Egzaktna funkcija
yspline = kspline(xtocke) # Aproksimacija funkcije

pl.figure()
pl.plot(xcvorovi, ycvorovi, 'o', xtocke, yspline, '--', xtocke, ytocke, 'g-')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.legend(['cvorovi', 'kubicni spline', 'funkcija'])
pl.grid()
pl.show()





from numpy import *
import scipy.integrate as spi
from scipy import interpolate as i
import pylab as pl

def f(x):
    return e**x

# Definiramo pocetak i kraj segmenta, te poloviste koje
# nam treba za Simpsonovu formulu

a = 0.0
b = 3.0
c = (a+b) / 2.

x1 = array([a, b])
x2 = array([a, c, b])

y1 = f(x1)
y2 = f(x2)

print('x1=', x1)
print('y1=', y1)

print('x2=', x2)
print('y2=', y2)

iTrap = spi.trapz(y1, x1)
iSimp = spi.simps(y2, x2)

print('Vrijednost integrala dobivena trapeznom formulom: ', iTrap)
print('Vrijednost integrala dobivena simpsonovom formulom: ', iSimp)

# Newton - Leibnitz
integral = e**3 - e**0

print('Vrijednost integrala: ', integral)

print('Prava greska trapezne formule je: ', iTrap - integral)
print('Prava greska simpsonove formule je: ', iSimp - integral)

M2 = e**3
M4 = e**3

apsGrTrap = (((b-a)**3) / 12) * M2
apsGrSimp = ((b-a)/2)**5 * (M4/90)

print('Apsolutna greska trapezne formule je: ', apsGrTrap)
print('Apsolutna greska simpsonove formule je: ', apsGrSimp)

pL = i.lagrange(x2, y2)
print('Kvadratni polinom kojim aproksimiramo f(x)=e**x je: ', pL)

xtocke = linspace(a, b, 50)
pl.plot(xtocke, f(xtocke), x1, y1, xtocke, pL(xtocke))
pl.legend(['funkcija', 'iTrap', 'iSimp'])
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.grid()
pl.fill_between(xtocke, f(xtocke))
pl.show()





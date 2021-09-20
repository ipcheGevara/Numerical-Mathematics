from numpy import *
import scipy.integrate as spi
from scipy import interpolate as i
import pylab as pl

def f(x):
    return sin(x)

a = 0.0
b = 3.0
eps = 1.e-4

def AbsD2f(x):
    return abs(-sin(x))

xtocke = linspace(a, b, 100)
pl.plot(xtocke, AbsD2f(xtocke), pi/2, AbsD2f(pi/2), 'yo')
pl.grid()
pl.show()


M2 = AbsD2f(pi/2)
n = ceil((b-a) * sqrt((M2/eps)*(b-a)/12.))
print('Broj potrebnih segmenata na koji treba podijeliti pocetni segment: ', n)

print('Realizacija integrala trapezne na dva nacina')
x = linspace(a, b, 151)
y = f(x)

iTrap = spi.trapz(y, x)
print('Rjesenje na prvi nacin: ', iTrap)

h = (b-a) / n
iPTrap = h/2. * (y[0] + 2*sum(y[1:int(n)]) + y[int(n)])
print('Rjesenje na drugi nacin: ', iPTrap)

integral = 1.989992497
print('Egzaktna vrijednost integrala: ', integral)

apsGrTrap = ((b-a)/12.) * h**2 * M2
print('Apsolutna greska trapezne formule je <=', apsGrTrap)

    
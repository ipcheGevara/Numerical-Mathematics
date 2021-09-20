# Produljena trapezna i produljena simpsonova
# koristeci 4 podsegmenta
# Izracunaj pravu i apsolutnu gresku

from numpy import *
import scipy.integrate as spi
from scipy import interpolate as i
import pylab as pl

def f(x):
    return log(x)

def AbsD2f(x):
    return abs(-(1./x**2))

def AbsD4f(x):
    return abs(-6./x**4)

a = 1
b = 3
n = 4
h = (b-a) / n

x = linspace(a, b, n+1) # 5 tocaka jer su 4 podsegmenta, moramo ukljuciti zadnji kraj s n+1
y = f(x)

print(x)
print(y)

print('Produljena trapezna na 2 nacina za realizaciju produljene trapezne')
iPTrap = h/2 * (y[0] + 2*sum(y[1:int(n)]) + y[int(n)])
iTrap = spi.trapz(y, x)
print('Vrijednost PTF na 1.nacin: ', iPTrap)
print('Vrijednost PTF na 2.nacin: ', iTrap)

print('Produljena simpsonova na 2 nacina')
iPSimp = 0.
for i in range(0, n-1, 2):
    iPSimp = iPSimp + h/3. * (y[i] + 4*y[i+1] + y[i+2])
iSimp = spi.simps(y, x)
print('Vrijednost PSF na 1.nacin: ', iPSimp)
print('Vrijednost PSF na 2.nacin: ', iSimp)

integral = 3* log(3) - 2
print('Prava vrijednost integrala: ', integral)

print('Prava greska PTF je: ', abs(integral - iPTrap))
print('Prava greska PSF je: ', abs(integral - iPSimp))

M2 = AbsD2f(1.)
M4 = AbsD4f(1.)

print('Apsolutna greska iPTrap je <=: ', ((b-a)/12.) * h**2 * M2)
print('Apsolutna greska iSimp je <= ', ((b-a)/180.) * h**4 * M4)


from numpy import *
import scipy.integrate as spi
from scipy import interpolate as i
import pylab as pl

def f(x):
    return sin(x)

def AbsD2f(x):
    return abs(-sin(x))

def AbsD4f(x):
    return abs(sin(x))

a = 0.0
b = 3.0
eps = 1.e-4

xtocke = linspace(a, b, 100)
y = f(xtocke)
pl.plot(xtocke, AbsD4f(xtocke), pi/2, AbsD4f(pi/2.), 'yo')
pl.grid()
pl.show()

M4 = AbsD4f(pi/2)

n = ceil((b-a) * ((M4*(b-a)) / (180*eps)) ** (1/4.))
print('Broj potrebnih cvorova za upotrebu PSF: ', n)



if n%2 != 0:
    print('n je neparan!')
    m = int(n) + 1
else:
    m = int(n)
    print('Broj potrebnih segmenata je: ', m)
    
print('Sada je novi broj segmenata m=', m)

x = linspace(a, b, m+1)
y = f(x)
iSimp = spi.simps(y, x)
print('Vrijednost integrala PSF na prvi nacin je: ', iSimp)

h = (b-a)/m
iPSimp = 0.0
for i in range(0, m-1, 2):
    iPSimp += h/3 *(y[i] + 4*y[i+1] + y[i+2])
print('Vrijednost integrala PSF na drugi nacin je: ', iPSimp)

integral = -cos(3.) + cos(0.)
print('Egzaktna vrijednost integrala: ', integral)
apsGrSimp = ((b-a) / 180.) * h**4 * M4
print('Apsolutna greska PSF je <=', apsGrSimp)
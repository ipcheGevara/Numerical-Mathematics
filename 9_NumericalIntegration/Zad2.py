from numpy import *
import scipy.integrate as spi
from scipy import interpolate as i
import pylab as pl

def f(x):
    return x**2 + x

a = 0.0
b = 3.0
c = (a+b) / 2

x1 = array([a, b])
y1 = f(x1)
x2 = array([a, c, b])
y2 = f(x2)

iTrap = spi.trapz(x1, y1)
iSimp = spi.simps(x2, y2)

print('Trapeznom formulom dobivamo: ', iTrap)
print('Simpsonovom formulom dobivamo: ', iSimp)

integral = 3**3 / 3. +3**2/2.

print('Egzaktna vrijednost integrala: ', integral)
print('Prava greska trapezne formule: ', abs(iTrap - integral))
print('Prava greska simpsonove formule: ', abs(iSimp - integral))

M2 = 2
M4 = 0

print('Apsolutna greska trapezne formule: ', (((b-a)**3.) / 12.) * M2) 
print('Apsolutna greska simpsonove formule: ', (((b-a)/2)**5) * M4 )
print('U ovom slucaju je Simpsonova formula egzaktna jer je apsolutna greska 0')

# Kreiramo interpolacijski polinom kako bi nacrtali Simpsonovu funkciju
pL = i.lagrange(x2, y2)

# Crtanje
xtocke = linspace(a, b, 100)
ytocke = f(xtocke)
pl.plot(xtocke, ytocke, x1, y1, xtocke, pL(xtocke), x2, y2)
pl.legend(['funkcija', 'iTrap', 'iSimp', 'Produljena trapezna varijanta'])
pl.fill_between(xtocke, ytocke, color='LightBlue')
pl.show()





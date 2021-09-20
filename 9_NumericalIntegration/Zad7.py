# Produljena trapezna, tocnost 10**-3
# izracunaj povrsinu grafom omedene funkcije
# pravcima x=2.5 i x=3 te x-osi. Graficki prikazite pravce i funkciju
# te obojite povrsinu koju zatvaraju s x-osi

from numpy import *
import scipy.integrate as spi
from scipy import interpolate as i
import pylab as pl

def f(x):
    return x**3-2*x**2-1

def AbsD2f(x):
    return abs(6*x-4)

a = 2.5
b = 3.0
eps = 1.e-3

#Racunannje broja podsegmenata na koji treba podijeliti pocetni segment zbog 
#zadane tocnosti

xtocke = linspace(2.5, 3, 100)
pl.plot(xtocke, AbsD2f(xtocke), 3., AbsD2f(3.), 'yo')
pl.grid()
pl.show()

M2 = AbsD2f(3.)
n = ceil((b-a)*sqrt((M2*(b-a))/(12.*eps)))
print('Broj podsegmenata na koji treba podijeliti pocetni segment je: ', n)

x = linspace(a, b, int(n)+1)
y = f(x)
iTrap = spi.trapz(y, x)
print('Rjesenje produljenom trapeznom formulom je: ', iTrap)

h = (b-a)/n
iPTrap = h/2*(y[0]+2*sum(y[1:int(n)])+y[int(n)])
print('Rjesenje produljenom trapeznom formulom je: ', iPTrap)

integral = 3**4/4.-2.5**4/4-2*(3**3/3-2.5**3/3)-3+2.5
print('Prava vrijednost integrala je: ', integral)

# Prvi pravac, 1.5 -> 0, 5 -> 0
# Ako sve x-eve saljemo u 0 to znaci da je y = 0 te smo dobili x-os
xpravac = [1.5, 5]
ypravac = [0, 0]

# Drugi pravac
# 2.5 -> -5, 2.5 -> 20
# doslovce smo dobili pravac gdje je x=2.5, tj. crtamo pravac x=2.5
# za ipsilon zapravo moze bilo koja vrijednost
xpravac1 = [2.5, 2.5]
ypravac1 = [-5, 20]

# Treci pravac
# 3->5, 3->20 --- crtamo pravac x=3.5
xpravac2 = [3, 3]
ypravac2 = [-5, 20]

xtocke2 = linspace(a-1, b+1, 100)
pl.plot(xtocke2, f(xtocke2), xpravac1, ypravac1, xpravac2, ypravac2, xpravac, ypravac)
pl.legend(['funkcija', 'x=2.5', 'x=3', 'x-os'])
pl.fill_between(xtocke, f(xtocke), color='LightBlue')
pl.grid()
pl.show()



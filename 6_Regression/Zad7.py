# Zadane su tocke u ravnini
# xi 
# yi
# Odredite a i b tako da fja f(x) = a*x**b najbolje aproksimira
# dane podatke u smislu metode najmanjih kvadrata

from numpy import *
import pylab as pl

x = [0.5, 1.0, 1.5, 2.0, 2.5]
y = [0.49, 1.60, 3.36, 6.44, 10.16]

lnx = log(x)
lny = log(y)

print(lnx)
print(lny)

koef = polyfit(lnx, lny, 1)
print('Koeficijenti reg pravca: ')
print(koef)

RegPravac = poly1d(koef)
print('Regresijski pravac: ')
print(RegPravac)

a = exp(RegPravac[0])
b = RegPravac[1]

print('a=', a)
print('b=', b)

print('Trazena funkcija je y=%s * x^(%s)' % (a, b))

def PotFja(x):
    return a*x**b

xtocke = linspace(min(x)-0.5, max(x)+0.5, 100)
yPotFja = PotFja(xtocke)
pl.plot(x, y, 'o', xtocke, yPotFja, 'm-')
pl.grid()
pl.show()



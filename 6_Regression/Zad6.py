# Eksperimentom je utvrden sljedeci broj mikroorganizama nakon proteka x sati
# (xi je vrijeme promatranja, a yi je izmjereni broj mikroorganizama u trenutku xi)
# xi 0 2 4 6 8 10 12 16
# yi 25 36 52 68 85 104 142 260
# Odredite jednadzbu krivulje regresije oblika y = ae**bx, te podatke prikazite graficki
# Procijenite broj mikroorganizama nakon 18h

from numpy import *
import pylab as pl

x = [0, 2, 4, 6, 8, 10, 12, 16]
y = [25, 36, 52, 68, 85, 104, 142, 260]

lny = log(y)
print(lny)

# Odredujemo koeficijente regresijskog pravca listu 
koef = polyfit(x, lny, 1)
RegPravac = poly1d(koef)

print('Regresijski pravac:')
print(RegPravac)

# Sad odredujemo koeficijente a i b koji nam trebaju za regresijsku krivulju
# koja je eksponencijalnog oblika

print('Slobodni koeficijent: ', RegPravac[0])
print('Vodeci koeficijent: ', RegPravac[1])

a = exp(RegPravac[0])
b = RegPravac[1]

print('a=', a)
print('b=', b)

def ExpFja(x):
    return a*exp(b*x) #y = a*e^(b*x)

xtocke = linspace(min(x)-0.5, max(x)+0.5, 100)
yExp = ExpFja(xtocke)
pl.plot(x, y, 'yo', xtocke, yExp, 'r-')
pl.grid()
pl.show()

print('Broj mikroorganizama nakon 18h je: ', ExpFja(18))




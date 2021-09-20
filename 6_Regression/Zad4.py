# metodom najmanjih kvadrata odredite polinome prvog i drugog stupnja
# koji aproksimiraju podatke:
# xi 0 0.4 0.8 1.2 1.6 2.0
# f (xi ) = yi 0.21 1.25 2.31 2.70 2.65 3.20
# Graficki priakzite dobivene regresijske polinome te pomocu njih odredite f(1.4)

from numpy import *
import pylab as pl

x = [0, 0.4, 0.8, 1.2, 1.6, 2.0]
y = [0.21, 1.25, 2.31, 2.7, 2.65, 3.2]

koef1 = polyfit(x, y, 1)
koef2 = polyfit(x, y, 2)

print('Koeficijenti regresijskog polinoma 1.st: ', koef1)
print('Koeficijenti regresijskog polinoma 2.st: ', koef2)

RegPolinom1 = poly1d(koef1)
RegPolinom2 = poly1d(koef2)

print('Regresijski polinom 1.st je:')
print(RegPolinom1)
print('Regresijski polinom 2.st je:')
print(RegPolinom2)


xtocke = linspace(min(x)-0.5, max(x)+0.5, 100)
yRegPolinom1 = RegPolinom1(xtocke)
yRegPolinom2 = RegPolinom2(xtocke)
pl.plot(x, y, 'yo', xtocke, yRegPolinom1, 'g-', xtocke, yRegPolinom2, 'r-')
pl.legend(['cvorovi', 'regresijski polinom 1.st', 'regresijski polinom 2.st'])
pl.grid()
pl.show()

print('p1(1.4)=', RegPolinom1(1.4))
print('p2(1.4)=', RegPolinom2(1.4))
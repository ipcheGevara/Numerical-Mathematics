# Nadite i graficki prikazite regresijski pravac i regresijski polinom
# drugog stupnja za podatke

from numpy import *
import pylab as pl

x = [1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7]
y = [6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828]

koef1 = polyfit(x, y, 1)
koef2 = polyfit(x, y, 2)

RegPolinom1 = poly1d(koef1)
RegPolinom2 = poly1d(koef2)

print('Regresijski polinom 1.st:')
print(RegPolinom1)
print('Regresijski polinom 2.st:')
print(RegPolinom2)

xtocke = linspace(min(x)-0.5, max(x)+0.5, 100)
yRegPolinom1 = RegPolinom1(xtocke)
yRegPolinom2 = RegPolinom2(xtocke)
pl.plot(x, y, 'yo', xtocke, yRegPolinom1, 'g-', xtocke, yRegPolinom2, 'b-')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.legend(['cvorovi', 'Regresijski polinom 1.st', 'Regresijski polinom 2.st'])
pl.grid()
pl.show()
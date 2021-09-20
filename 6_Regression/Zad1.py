# Za navedene tocke odredite i graficki prikazite regresijski pravac
# xi 1 3 4 6 7
# yi 1 3 2 4 3

from numpy import *
import pylab as pl

x = [1, 3, 4, 6, 7] # lista x-eva
y = [1, 3, 2, 4, 3] # lista y-a

koef = polyfit(x, y, 1)
print('Koeficijenti regresijskog pravca su: ')
print(koef)

RegPravac = poly1d(koef)
print('Regresijski pravac je: ')
print(RegPravac)

yRegPravac = RegPravac(x)
print('y komponente tocaka koje leze na regresijskom pravcu')
print(yRegPravac)

pl.plot(x, y, 'yo', x, yRegPravac, 'b-')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.grid()
pl.show()




# Zadani su podaci o ulaganju u marketing i ostvarenom
# godisnjem profitu u 15 turistickih agencija
# Odredite jednadzbu regresijskog pravca i prikazite ga graficki
# Procijenite godisnji profit tvrtke koja bi u marketing ulozila 220 tisuca

from numpy import *
import pylab as pl

x = [15, 22, 25, 30, 40, 45, 50, 60, 70, 80, 95, 100, 120, 130, 150]
y = [80, 95, 100, 120, 110, 145, 130, 180, 210, 200, 280, 320, 350, 375, 480]

koef = polyfit(x, y, 1)
print('Koeficijenti regresijskog pravca: ')
print(koef)

RegPravac = poly1d(koef)
print('Jednadzba regresijskog pravca: ')
print(RegPravac)

yRegPravac = RegPravac(x)
print('y komponente regresijskog pravca su:')
print(yRegPravac)

pl.plot(x, y, 'yo', x, yRegPravac, 'g-')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.grid()
pl.show()

print('Godisnji profit ako bi ulozili 220k: ', RegPravac(220))


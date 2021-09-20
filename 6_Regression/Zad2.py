# Mjerenjem je ustanovljeno da elektricni otpor R bakrene zice
# ovisi o temperaturi t na sljedeci nacin
# t 19.1 25 30.1 36 40 45.1 50
# R 76.3 77.8 79.75 80.8 82.35 83.9 85.1
# Uz pretpostavku da se radi o linearnoj ovisnosti, odredite
# parametre a i b linearne funkcije R(t ) = at + b

from numpy import *
import pylab as pl

x = [19.1, 25., 30.1, 36., 40., 45.1, 50.]
y = [76.3, 77.8, 79.75, 80.8, 82.35, 83.9, 85.1]

koef = polyfit(x, y, 1)
print('Koeficijenti regresijskog pravca su:')
print(koef)

RegPravac = poly1d(koef, variable='t')
print('Regresijski pravac:')
print(RegPravac)

yRegPravac = RegPravac(x)
print('y komponente regresijskog pravca su:')
print(yRegPravac)

pl.plot(x, y, 'yo', x, yRegPravac, 'g-')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.grid()
pl.show()




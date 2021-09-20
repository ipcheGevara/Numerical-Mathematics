from numpy import *
import pylab as pl

def f(x):
    return x**2 + 4*sin(x) - 1

def Sekanta(a, b, eps, MaxIteracija=20):
    # Pocetni korak, pocetak i kraj
    print('0. iteracija: %s' % a)
    print('1. iteracija: %s' % b)
    i = 1
    while abs(b-a)>eps:
        i += 1
        xi = b - f(b) * (b-a)/f(b)-f(a)
        print('%s. iteracija: %s' % (i, xi))
        if f(xi) == 0:
            return xi, i
        else:
            a=b #pocetna (0.-ta) iteracija nestaje, druga postaje prva
            b=xi #b postaje onda novodobivena iteracija xi
        if i==MaxIteracija:
            print('Rjesenje nije dobiveno unutar max broja iteracija')
            break
    return xi, i
            

xn, i = Sekanta(-2.5, -2, 1.e-8)
print('x%s=%s', (i, xn))

xm, j = Sekanta(0, 0.5, 1.e-8)
print('x%s=%s', (j, xm))











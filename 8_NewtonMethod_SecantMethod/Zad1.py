# f(x)=x^5 - x^3 -2

from numpy import *
import pylab as pl

def f(x):
    return x**5 - x**3 - 2

# Nultocku mozemo locirati i smjestiti unutar segmenta [1, 1.5]
x  = linspace(1, 1.5, 100)
pl.plot(x, f(x), 'r-')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.grid()
pl.show()

def df(x):
    return 5*x**4 - 3*x**2

def d2f(x):
    return 20*x**3 - 6*x

def Newton(x, eps, MaxIteracija=30):
    if f(x)*d2f(x) < 0: # Nije zadovoljen uvjet f(x)*d2f(x)>0 pa nema konvergencije
        print('Izaberite drugu pocetnu aproksimaciju!')
    else:
        print('0. iteracija: %s' % x)
        i=1
        while i <= MaxIteracija:
            if abs(df(x)) < eps:
                print('Horizontalna tangenta')
                break
            dx = f(x) / df(x)
            x = x - dx
            print('%s. iteracija: %s' % (i, x))
            if abs(dx) < eps:
                return x, i
            else:
                i+=1
        print('Rjesenje do na zadanu tocnost nije moguce odrediti za definirani broj iteracija')


xn, i = Newton(1.5, 1.e-3)
print('x%s = %s' % (i, xn))





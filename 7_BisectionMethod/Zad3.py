# f(x) = x**2 + 4sinx - 1

from numpy import *
import pylab as pl

def f(x):
    return x**2 + 4*sin(x) - 1

x = linspace(-3, 2, 100)
pl.plot(x, f(x), 'b-')
pl.grid()
pl.show()

def Bisekcija(a, b, eps, MaxIteracija=30):
    xi = (a+b)/2.0
    i = 0
    print('%s. iteracija: %s' % (i, xi))
    while (b-a)/2.0 > eps:
        if f(xi)==0:
            return xi, i
        elif f(a)*f(xi) < 0:
            b=xi
        else:
            a=xi
        xi = (a+b)/2.0
        i = i+1
        print('%s. iteracija: %s' % (i, xi))
        if i==MaxIteracija:
            print('Nije pronadena vrijednost do na zadanu tocnost')
            break
    return xi, i

xn, i = Bisekcija(-2.5, 3, 1.e-8)
print('Rjesenje')
print('x%s = %s' % (i, xn))

xm, j = Bisekcija(0, 0.5, 1.e-8)
print('Rjesenje')
print('x%s = %s' % (j, xm))






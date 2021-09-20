# f(x) = x^5 - x^3 - 2

from numpy import *
import pylab as pl

def f(x):
    return x**5 - x**3 - 2

x = linspace(-2, 2, 100)
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

xn, i = Bisekcija(1.0, 1.5, 1.e-3)
print('Rjesenje')
print('x%s = %s' % (i, xn))
pl.plot(x, f(x), 'b-', xn, xn, 'y^')
pl.grid()
pl.show()





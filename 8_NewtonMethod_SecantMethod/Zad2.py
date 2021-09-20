from numpy import *
import pylab as pl

def f(x):
    return x**2 + 4*sin(x)-1

x = linspace(-5, 5, 100)
pl.plot(x, f(x))
pl.grid()
pl.show()

def df(x):
    return 2*x + 4*cos(x)

def d2f(x):
    return 2 - 4*sin(x)

def Newton(x, eps, MaxIteracija=20):
    if f(x) * d2f(x) < 0:
        print('Odrediti drugu pocetnu aproksimaciju - nema konvergencije')
    else:
        print('0. iteracija: %s' % x)
        i = 1
        while i<=MaxIteracija:
            if abs(df(x)) < eps:
                print('Horizontalna tangenta')
                break
            dx = f(x) / df(x)
            x = x - dx
            print('%s. iteracija: %s' % (i, x))
            if abs(dx) < eps:
                return x, i
            else:
                i = i+1
        print('Rjesenje u zadanom broju iteracija nije pronadeno!')
        
xn, i = Newton(-2.5, 1.e-8)
print('x%s = %s' % (i, xn))

xm, j = Newton(0.5, 1.e-8)
print('x%s = %s' % (j, xm))

x = linspace(-3, 3, 100)
pl.plot(x, f(x), 'r-', xn, f(xn), 'g^', xm, f(xm), 'b^')
pl.grid()
pl.show()








# Metodom bisekcije nadite rjesenje jednadzbe x=e**(-x) s tocnoscu 10**(-8)
# f(x) = x, f(x) = e^(-x)
# Sjeciste x=e**(-x) je zapravo nultocka funkcije f(x)=x-e^(-x)

from numpy import * 
import pylab as pl

x = linspace(-2, 2, 100)
pl.plot(x, x, 'r-', x, e**(-x), 'b')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.grid()
pl.show()

def f(x):
    return x-e**(-x)

x = linspace(-2, 2, 100)
pl.plot(x, f(x), 'b-')
pl.xlabel('x-os')
pl.ylabel('y-os')
pl.grid()
pl.show()

# Iz grafa se vidi da je trazena nultocka unutar segmenta [0.5, 1]

def Bisekcija(a, b, eps, MaxIteracija=30):
    xi = (a+b)/2.0 # Poloviste
    i = 0
    print('%s. iteracija: %s ' % (i, xi))
    while (b-a)/2.0 > eps:
        if f(xi) == 0:
            return xi, i
        elif f(a)*f(xi)<0:
            b=xi
        else:
            a=xi
        xi = (a+b)/2.0
        i=i+1
        print('%s. iteracija: %s ' % (i, xi))
        if i==MaxIteracija:
            print('Rjesenje do na zadanu tocnost unutar maksimalnog broja iteracija nije postignuto')
            break
    return xi, i


xn, i = Bisekcija(0.5, 1, 10**(-8))
print('Rjesenje')
print('x%s = %s' % (i, xn))

pl.plot(x, x, 'r-', x, e**(-x), 'b-')
pl.plot(xn, xn, 'go', xn, e**(-xn), 'y^')
pl.grid()
pl.show()



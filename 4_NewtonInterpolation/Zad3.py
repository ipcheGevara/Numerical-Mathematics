#Formirajte Newtonov interpolacijski polinom koji zadovoljava uvjete:
#p(0) = -1, p(2) = 2, p(6) = 3.

from numpy import * 

x = array([0, 2, 6]) # cvorovi
y = array([-1, 2, 3])

n = len(x)
a = []

for i in range(n):
    a.append(y[i])

for j in range(1, n):
    for i in range(n-1, j-1, -1):
        a[i] = float(a[i] - a[i-1]) / float(x[i] - x[i-j])
        
print(x)
print(y)
print('Koeficijenti NIP-a:')
print(a)
print('NIP: ')
print('P2(x)=',a[0],'+',a[1],'(x-',x[0],')+',a[2],'(x-',x[0],')(x-',x[1],')')
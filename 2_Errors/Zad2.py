# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:24:02 2021

@author: ipcheGevara
"""

# Izracunajte sumu niza prvih 10**6 clanova niza
# ai = 1/i, i=1,2,...

from decimal import *
getcontext().prec = 45

sumaNaprijed = 0
sumaNazad = 0

for i in range(1, 10**6+1):
    sumaNaprijed = Decimal(sumaNaprijed) + Decimal(1./i**2)
    
print(sumaNaprijed)

for i in range(10**6, 0, -1):
    sumaNazad = Decimal(sumaNazad) + Decimal(1./i**2)
    
print(sumaNazad)

print("Suma naprijed: ", sumaNaprijed)
print("Suma nazad: ", sumaNazad)

apsGr = abs(sumaNaprijed - sumaNazad)

print("Apsolutna greska suma: ", apsGr)


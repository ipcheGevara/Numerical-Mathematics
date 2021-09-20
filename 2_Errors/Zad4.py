# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:55:51 2021

@author: ipcheGevara
"""

# Izracunati relativnu i apsolutnu gresku
# priblizne vrijednosti x* = 0.3 i broja x=1/3

from decimal import *
getcontext().prec = 28

x1 = 0.3
x2 = Decimal(1./3)

apsGr = abs(Decimal(x2) - Decimal(x1))
relGr = apsGr / Decimal(x1)

print("Apsolutna greska iznosi: ", apsGr)
print("Relativna greska iznosi: ", relGr)
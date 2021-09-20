# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:00:55 2021

@author: ipcheGevara
"""

# Ocijeniti na sedam decimala relativnu i 
# apsolutnu gresku priblizne vrijednosti
# x* = 1.41 i broja x=sqrt(2)

from math import * 
from decimal import *
getcontext().prec = 7

x1 = 1.41
x2 = sqrt(2)

print("x1= ", x1)
print("x2= ", x2)

apsGr = abs(x2 - x1)
relGr = apsGr / abs(x1)

print("Apsolutna greska iznosi: ", apsGr)
print("Relativna greska iznosi: ", relGr)



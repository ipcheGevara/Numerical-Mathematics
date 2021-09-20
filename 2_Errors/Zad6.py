# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:29:14 2021

@author: ipcheGevara
"""

from decimal import *
import numpy as np

getcontext().prec = 28

a = np.pi
b = np.pi + 10**(-10)

zaokruzeniA = round(a, 12)
zaokruzeniB = round(b, 13)

apsGrA = abs(a - zaokruzeniA)





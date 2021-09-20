# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:40:51 2021

@author: ipcheGevara
"""

# Zaokruzi PI na tri decimale i odredi
# apsolutnu i relativnu gresku te aproksimacije

import numpy as np
from decimal import *

praviPi = np.pi

zaokruzeniPi = round(np.pi, 3)

apsGr = abs(Decimal(praviPi) - Decimal(zaokruzeniPi))
relGr = abs(abs(praviPi - zaokruzeniPi)/abs(praviPi))

print("Apsolutna greska: ", apsGr)
print("Relativna greska: ", relGr)
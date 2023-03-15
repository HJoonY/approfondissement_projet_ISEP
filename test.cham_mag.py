import math
import matplotlib.pyplot as plt
import numpy
from decimal import Decimal
from fonction_valeurdecable import *
from fonction_cham_mag import *

R1 = 0.3
R2 = 0.7
I1 = 5
I2 = 5
choix_R1 = 2
choix_R2 = 1
x = 0.5

print("sortie :",round(cham_mag(x,R1,R2,choix_R1,choix_R2,I1,I2),16))
print("validé")
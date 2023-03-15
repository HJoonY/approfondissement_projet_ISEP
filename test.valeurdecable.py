import math
import matplotlib.pyplot as plt
import numpy
# from decimal import Decimal
from fonction_valeurdecable import *


R1 = 0.3
R2 = 0.7

print("<<cas 1>>")
print("sortie :",round(valeurdecable(R1,0.5,2,5),7))


print("<<cas 2>>")
print("sortie:",round(valeurdecable(R2,0.5,2,5),7))

print("<<cas 3>>")
print("sortie :",round(valeurdecable(R2,0.5,1,5),16))

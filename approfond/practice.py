import math
import numpy
from decimal import Decimal

mu = (4 * math.pi) * (10 ** (-7))
valeurdeI = 1

ordredeR = 0.4


def calcul(positiondeR):
    valeur = Decimal((mu * valeurdeI * positiondeR) / (2 * math.pi * (ordredeR) ** 2))
    return valeur
positiondeR = numpy.arange(0,float(ordredeR)*3,0.0001)
grap_y = [(calcul(i)) for i in positiondeR]
print(grap_y)

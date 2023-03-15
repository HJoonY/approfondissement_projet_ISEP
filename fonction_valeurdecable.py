import math
import matplotlib.pyplot as plt
import numpy
from decimal import Decimal

#--------------------------------------
# Créé par HJ.YOO
# Renvoi La valeur de champe magentique par rapport un point R
# VERSION :  1.0     20/09/2021      Projet4
# ENTREES :     l’ordre de R : soit R1 soit R2
#               postiondeR :   la position de r en mètre entre 0 et N ( l'utilisateur va inserer la valuer N)
#               choix: un type de cable soit 1 soit 2
#               valeurdeI:    la valeur de I
#SORTIES :      la valeur de champ magnetique
#--------------------------------------

def valeurdecable(ordredeR, postiondeR, choix, valeurdeI):
    mu = (4 * math.pi) * (10 ** (-7))
    if choix == 1:
        if postiondeR < ordredeR:
            valeur = Decimal((mu * valeurdeI * postiondeR) / (2 * math.pi * ((ordredeR) ** 2)))
        else:
            valeur = Decimal((mu * valeurdeI) / (2 * math.pi * postiondeR))
    else:
        if postiondeR < ordredeR:
            valeur = 0
        else:
            valeur = Decimal((mu * valeurdeI) / (2 * math.pi * postiondeR))
    return valeur


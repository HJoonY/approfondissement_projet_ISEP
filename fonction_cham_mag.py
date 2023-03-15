import math
import matplotlib.pyplot as plt
import numpy
from decimal import Decimal
from fonction_valeurdecable import *

#--------------------------------------
# Créé par HJ.YOO
# Renvoi La valeur de champe magentique par rapport un point R
# VERSION :  1.0     20/09/2021      Projet4
# ENTREES :     x :  la position ( la valeur de R)
#               R1 : le rayon de R1
#               R2 : le rayon de R2
#               choix_R1: un type de cable soit 1 soit 2 de R1
#               choix_R2: un type de cable soit 1 soit 2 de R2
#               I1 :    la valeur de I1
#               I2 :    la valeur de I2
#SORTIES :      valeyr la somme des valeurs de champ magnetique en R
#--------------------------------------

def cham_mag(x, R1, R2, choix_R1, choix_R2, I1, I2):
    valeur = Decimal(valeurdecable(R1, x, choix_R1, I1)) + Decimal(valeurdecable(R2, x, choix_R2, I2))
    return valeur

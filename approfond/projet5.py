## En tete - 작성 하기 ##

import cv2
import math
import matplotlib.pyplot as plt
import numpy

# fname = '/Users/Joon/Desktop/ISEP/I2/approfond/photo.png'
# img = cv2.imread(fname, cv2.IMREAD_COLOR)
#
# cv2.namedWindow('Champ magnétique d’un câble coaxial', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Champ magnétique d’un câble coaxial', 100, 50)


def typedecable(x):
    if x == 1:
        print(
            "** Vous avez choisir un cylindre de rayon R parcouru par un courant d’intensité I uniformément réparti dans la section du cylindre")
    elif x == 2:
        print(
            "** Vous avez choisir un cylindre de rayon R parcouru par un courant d’intensité I uniformément réparti à la surface du cylindre")
    return x


# --------------------------------------
# Créé par HJ.YOO
# Renvoi La choix de type de cable
# VERSION :  1.0     20/09/2021      Projet4
# ENTREES :     x   choix
#
# SORTIES :      x  soit 1 soit 2 ca depends du choix
#                  et annonce son choix par print()
# --------------------------------------

print('''

**** Bienvenue de simulation numérique de la Physique avec Pyton ****

On considère un câble coaxial infini cylindrique constitué (voir figure, et tapez l'espace) : I

Vous pouvez choisir un type de cable soit un courant I réparti dans son volume soit uniformément réparti à la surface 

Vous devez inserer des chiffres de R1(Rayon de cylindre interieur),R2(Rayon de cylindrique exterieur),I1(Intensité de cylindre interieur) et I2(Intensité de cylindre exterieur).
''')

# cv2.imshow('Champ magnétique d’un câble coaxial', img)
# cv2.waitKey(0)

# vrai_R1 = float(input("Inserer la valeur de R1(Rayon de cylindre interieur): "))
# vrai_R2 = float(input("Inserer la valeur de R2(Rayon de cylindrique exterieur) : "))
# while (vrai_R2 <= vrai_R1):
#     R2 = float(input(
#         "Il faut R2 etre superieur que R1(Rayon de cylindre interieur) ,Inserer la valeur de R2(Rayon de cylindrique exterieur) : "))
#
# R1 = 1
# R2 = (vrai_R2/vrai_R1)

R1 = float(input("Inserer la valeur de R1(Rayon de cylindre interieur): "))
R2 = float(input("Inserer la valeur de R2(Rayon de cylindrique exterieur) : "))
while (R2 <= R1):
    R2 = float(input("Il faut R2 etre superieur que R1(Rayon de cylindre interieur) ,Inserer la valeur de R2(Rayon de cylindrique exterieur) : "))

choix_R1 = int(input('''Quel type de cable 1 vous voulez mettre?
                      pressez 1 pour cable avec un courant I réparti dans son volume 
                      pressez 2 pour un cable avec un courant I reparti dans son surface  : '''))
while (choix_R1 != 1 and choix_R1 != 2):
    print("Vous devez choisir 1 ou 2")
    choix_R1 = int(input('''Quel type de cable 1 vous voulez mettre?
    pressez 1 pour cable avec un courant I réparti dans son volume
    pressez 2 pour un cable avec un courant I reparti dans son surface  : '''))
typedecable(choix_R1)
print("\n")
choix_R2 = int(input('''Quel type de cable 2 vous voulez mettre?
                      pressez 1 pour cable avec un courant I réparti dans son volume 
                      pressez 2 pour un cable avec un courant I reparti dans son surface  : '''))

while (choix_R2 != 1 and choix_R2 != 2):
    print("Vous devez choisir 1 ou 2")
    choix_R1 = int(input('''Quel type de cable 2 vous voulez mettre?
                          pressez 1 pour cable avec un courant I réparti dans son volume
                          pressez 2 pour un cable avec un courant I reparti dans son surface  : '''))
typedecable(choix_R2)
print("\n")

print("Pour avoir un câble coaxial, I1 + I2 doit etre egal à 0")
I1 = float(input("Inserer la valeur de I1 (Intensité de cylindre interieur) : "))
print("La valeur d'I1 ", I1, 'A')
I2 = float(input("Inserer la valeur de I2 (Intensité de cylindre exterieur) : "))
print("La valeur d'I2 ", I2, 'A')


def valeurdecable(ordredeR, postiondeR, choix, valeurdeI):
    mu = (4 * math.pi) * 10 ** (-7)
    if choix == 1:
        if postiondeR < ordredeR:
            valeur = (mu * valeurdeI * postiondeR) / (2 * math.pi * (ordredeR) ** 2)
        else:
            valeur = (mu * valeurdeI) / (2 * math.pi * postiondeR)
    else:
        if postiondeR < ordredeR:
            valeur = 0
        else:
            valeur = (mu * valeurdeI) / (2 * math.pi * postiondeR)
    return valeur


# --------------------------------------
# Créé par HJ.YOO
# Renvoi La valeur de champe magentique par rapport un point R
# VERSION :  1.0     20/09/2021      Projet4
# ENTREES :     ordredeR   l'ordre de cylindrique
#               postiondeR   une position de R
#               choix        type de cable (1 pour cable avec un courant I réparti dans son volume
#                                            2 pour un cable avec un courant I reparti dans son surface)
#               valeurdeI    la valeur de I
# SORTIES :      valeyr la valeur de champ magnetique
# --------------------------------------
def cham_mag(x):
    valeur = valeurdecable(R1, x, choix_R1, I1) + valeurdecable(R2, x, choix_R2, I2)
    return valeur


# --------------------------------------
# Créé par HJ.YOO
# Renvoi La valeur de champe magentique par rapport un point R
# VERSION :  1.0     20/09/2021      Projet4
# ENTREES :     x la position ( la valeur de R)
# SORTIES :      valeyr la somme des valeurs de champ magnetique
# --------------------------------------

grap_x = numpy.arange(0, int(R2) * 2, 0.001)
grap_y = [cham_mag(i) for i in grap_x]
plt.plot(grap_x, grap_y, label="La valeur de Champ magnetique")
plt.axvline(x=R1, linestyle='--', color='red', label="R1")
plt.axvline(x=R2, linestyle='--', color='green', label="R2")
plt.xlabel('La valeur de R (La distance proportion, R1 = 1)')
plt.ylabel('La valeur de Champ magnetique')
plt.legend(fontsize=7)
plt.grid()
plt.show()

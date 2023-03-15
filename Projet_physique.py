import math
import matplotlib.pyplot as plt
import numpy
from decimal import Decimal
from fonction_typedecable import *
from fonction_valeurdecable import *
from fonction_cham_mag import *

entree = '''

**** Bienvenue dans la simulation de la Physique avec Pyton ****

On considère un câble coaxial infini cylindrique constitué : I

Vous pouvez choisir un type de câble soit un courant I réparti dans son volume soit uniformément réparti à la surface 

Vous devez insérer des chiffres de R1(Rayon de cylindrique intérieur en mètre),R2(Rayon de cylindrique exterieur en mètre),
I1(Intensité de cylindre intérieur en Ampère) et I2(Intensité de cylindre extérieur en Ampère).

'''

print(entree)


R1 = float(input("Insérer la valeur de R1(Rayon de cylindrique intérieur): "))
R2 = float(input("Insérer la valeur de R2(Rayon de cylindrique extérieur) : "))
print("\n")
while R2 <= R1:
    R2 = float(input(
        "Il faut que R2 soit supérieur à R1(Rayon de cylindrique intérieur) ,Insérer la valeur de R2(Rayon de cylindrique extérieur) : "))

choix_R1 = int(input('''Quel type de câble 1 voulez-vous mettre?
                      pressez 1 pour câble avec un courant I réparti dans son volume 
                      pressez 2 pour un câble avec un courant I réparti dans sa surface  : '''))

while choix_R1 != 1 and choix_R1 != 2:
    print("Vous devez choisir 1 ou 2")
    choix_R1 = int(input('''Quel type de câble 1 voulez-vous mettre?
                          pressez 1 pour câble avec un courant I réparti dans son volume 
                          pressez 2 pour un câble avec un courant I réparti dans sa surface  : '''))
typedecable(choix_R1)
print("\n")
choix_R2 = int(input('''Quel type de câble 2 voulez-vous mettre?
                          pressez 1 pour câble avec un courant I réparti dans son volume 
                          pressez 2 pour un câble avec un courant I réparti dans sa surface  : '''))

while choix_R2 != 1 and choix_R2 != 2:
    print("Vous devez choisir 1 ou 2")
    choix_R2 = int(input('''Quel type de câble 2 voulez-vous mettre?
                              pressez 1 pour câble avec un courant I réparti dans son volume 
                              pressez 2 pour un câble avec un courant I réparti dans sa surface  : '''))
typedecable(choix_R2)
print("\n")

print("Pour avoir un câble coaxial, I1 + I2 doit être égal à 0")
I1 = float(input("Insérer la valeur de I1 (Intensité du cylindre intérieur) : "))
print("La valeur d'I1 ", I1, 'A')
I2 = float(input("Insérer la valeur de I2 (Intensité du cylindre extérieur) : "))
print("La valeur d'I2 ", I2, 'A')

gap = (R2 - R1) / 1000
max_grap = float(input("Mettre la valeur maximum du rayon que vous voulez en mètre (il faut qu'il soit plus grand que R2) :"))
while max_grap < R2:
    max_grap = float(input("il faut mettre une chiffre plus grand que R2 :"))
grap_x = numpy.arange(0, max_grap, gap)
grap_y = [cham_mag(i, R1, R2, choix_R1, choix_R2, I1, I2) for i in grap_x]

questiondezero = ''' Vous voulez deviner ou savoir quand la valeur du champ est nulle (en mètre)? ( la valeur nulle = valeur absolue de 0,5% de la valeur maximum) 
Inserez 1 ou 2 pour deviner : 1  ou savoir la réponse tout de suite: 2 
votre choix : '''
print("\n")
choix = int(input(questiondezero))

des_valeurs = []
des_valeurs.append(abs(cham_mag(R1, R1, R2, choix_R1, choix_R2, I1, I2)))
des_valeurs.append(abs(cham_mag(R2, R1, R2, choix_R1, choix_R2, I1, I2)))

valeur_max = max(des_valeurs)
question_de_valeur_zero = '''" A partir de quel pourcentage de la valeur maximum, vous voulez considerer la valeur nulle ?
Inserer 10 pour 10% la valeur maximum , 1 pour 1% de la valeur maximum 
votre choix : '''
quand_valuer_zero = float(input(question_de_valeur_zero))
valeur_zero = Decimal(quand_valuer_zero*0.01)*valeur_max
index_valeur_max = int(des_valeurs.index(valeur_max))
quand_valeur_max = 0
if index_valeur_max == 0:
    quand_valeur_max = R1
else:
    quand_valeur_max = R2

valeur_en_nulle = R2
newx = cham_mag(valeur_en_nulle, R1, R2, choix_R1, choix_R2, I1, I2)

while abs(newx) > valeur_zero:
    valeur_en_nulle += gap
    newx = cham_mag(valeur_en_nulle, R1, R2, choix_R1, choix_R2, I1, I2)

if choix == 1:
    reponse = 0
    while (reponse != (valeur_en_nulle)):
        reponse = input('insérer votre réponse :')
        if reponse == 'jsp':
            break
    print("La valeur maximum est en ",quand_valeur_max,"m")
    print("voilà le champ est nul en ",valeur_en_nulle,"m", "la valeur nulle est",quand_valuer_zero,"% de la valeur maximum")
elif choix == 2:
    print("La valeur maximum est en ",quand_valeur_max,"m")
    print("voilà le champ est nul en ",valeur_en_nulle,"m", "la valeur nulle est",quand_valuer_zero,"% de la valeur maximum")

plt.plot(grap_x, grap_y, label="La valeur du champ magnétique")
plt.axvline(x=R1, linestyle='--', color='red', label="R1")
plt.axvline(x=R2, linestyle='--', color='green', label="R2")
plt.xlabel('La valeur de R en mètre')
plt.ylabel('La valeur du champ magnétique')
plt.legend(fontsize=7)
plt.grid()
plt.show()

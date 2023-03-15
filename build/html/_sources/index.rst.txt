projet_physique
===========================================================

def typedecable(x):
    Ce fonction est de choisir un type de cable

    :param x: soit 1 soit 2
    :return: une phrase et int(x)
    :exemple:
typedecable(1):
    return :x = 1 avec l'affichage "Vous avez choisir un cylindre de rayon R parcouru par un courant d’intensité I uniformément réparti dans la section du cylindre"

typedecable(2):
    return :x=2 avec l'affichage "Vous avez choisir un cylindre de rayon R parcouru par un courant d’intensité I uniformément réparti à la surface du cylindre"

---------------

def valeurdecable(ordredeR, postiondeR, choix, valeurdeI):
    Ce fonction est de calcuer la valeur de magnetique en postiondeR (en mètre)

    :param ordredeR: l'ordre de R : soit R1 soit R2
    :param postiondeR: la position de r en mètre entre 0 et n (n =  c'est utilisatuer qui va decider)
    :param choix: un type de cable soit 1 soit 2
    :param valeurdeI: valeur de I
    :return: valeur de magnétique
    :exemple:
valeurdecable(R1,0.5,2,5): # avec R1 : 0.3 m et R2 0.7m
return = 0.000002000000

valeurdecable(R2,0.5,2,5):
return = 0 (comme ce type de cable est intensité I uniformément réparti à la surface du cylindre)

valeurdecable(R2,0.5,1,5):
return = 0.00000102040

-----------

def cham_mag(x,R1,R2,choix_R1,choix_R2,I1,I2):
    Ce fonction fait calculer la somme de valeur magnétique.

    :param x: la valeur de R, c'est a dit position
    :param R1: le rayon de R1
    :param R2: le rayon de R2
    :param choix_R1: un type de cable de R1
    :param choix_R2: un type de cable de R2
    :param I1: la valeur de I1
    :param I2: la valeur de I2

    :return: la valeur total magnetique en R
    :exemple:

cham_mag(0.5): la meme condition que precedent(R1 : 0.3m, R2: 0.7m, I1 et I2 : 5 A)
return = 0.000003020408 (= valeurdecable(R1,0.5,2,5) + valeurdecable(R2,0.5,1,5))

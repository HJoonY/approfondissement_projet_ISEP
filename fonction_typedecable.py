#--------------------------------------
# Créé par HJ.YOO
# Renvoi La choix de type de cable
# VERSION :  1.0     20/09/2021      Projet4
# ENTREES :     x:   soit 1 soit 2
#
# SORTIES :      une phrase et int(x)
#--------------------------------------

def typedecable(x):
    if x == 1:
        print(
            "** Vous avez choisir un cylindre de rayon R parcouru par un courant d’intensité I uniformément réparti dans la section du cylindre")
    elif x == 2:
        print(
            "** Vous avez choisir un cylindre de rayon R parcouru par un courant d’intensité I uniformément réparti à la surface du cylindre")
    return x


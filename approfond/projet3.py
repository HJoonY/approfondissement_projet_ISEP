import cv2
import math
import matplotlib.pyplot as plt

fname = '/Users/Joon/Desktop/ISEP/I2/approfond/photo.png'
img = cv2.imread(fname,cv2.IMREAD_COLOR)

cv2.namedWindow('Champ magnétique d’un câble coaxial',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Champ magnétique d’un câble coaxial',100 ,50)
def typedecable(x):
    if x == 1:
        print(" Vous avez choisir un cylindre de rayon R parcouru par un courant d’intensité I uniformément réparti dans la section du cylindre")
    elif x == 2:
        print("Vous avez choisir un cylindre de rayon R parcouru par un courant d’intensité I uniformément réparti à la surface du cylindre")
    return x

print('''

Bienvenue de simulation numerique de la Physique avec Pyton.

On considère un câble coaxial infini cylindrique constitué (voir figure) : I

Vous pouvez choisir un type de cable soit un courant I réparti dans son volume
 soit uniformément réparti à la surface 
 
Vous pouvez inserer des chiffres de R1,R2,I1 et I2.
Pour connaitre un valeur numerique de magnetique en un point, vous pouvez inserer.

''')

cv2.imshow('Champ magnétique d’un câble coaxial',img)
cv2.waitKey(0)

R1 = float(input("Inserer la valeur de R1 : "))
R2 = float(input("Inserer la valeur de R2 : "))
if R2 <= R1:
    R2 = float(input("Il faut R2 etre superieur que R1 ,Inserer la valeur de R2 : "))

choix_R1 = int(input('''Quel type de cable 1 vous voulez mettre?
                      pressez 1 pour cable avec un courant I réparti dans son volume 
                      pressez 2 pour un cable avec un courant I reparti dans son surface'''))
if choix_R1 != 1 and choix_R1 != 2:
    print("Vous devez choisir 1 ou 2")
    choix_R1 = int(input('''Quel type de cable 1 vous voulez mettre?
    pressez 1 pour cable avec un courant I réparti dans son volume
    pressez 2 pour un cable avec un courant I reparti dans son surface'''))
print("\n")
typedecable(choix_R1)
print("\n")
choix_R2 = int(input('''Quel type de cable 2 vous voulez mettre?
                      pressez 1 pour cable avec un courant I réparti dans son volume 
                      pressez 2 pour un cable avec un courant I reparti dans son surface'''))

if choix_R2 != 1 and choix_R2 != 2:
    print("Vous devez choisir 1 ou 2")
    choix_R1 = int(input('''Quel type de cable 2 vous voulez mettre?
                          pressez 1 pour cable avec un courant I réparti dans son volume
                          pressez 2 pour un cable avec un courant I reparti dans son surface'''))
print("\n")
typedecable(choix_R2)
print("\n")

print("Pour avoir un câble coaxial, I1 + I2 doit etre egal à 0")
I1 = float(input("Inserer la valeur de I1 : "))
print("La valeur d'I1 ",I1,'A')
I2 = float(input("Inserer la valeur de I2 : "))
print("La valeur d'I2 ",I2,'A')

R = float(input("Inserer la valeur de R (point où vous etes ) "))



def valeurdecable(ordredeR,postiondeR,choix,valeurdeI):
    mu = (4 * math.pi) * 10 ** (-7)
    if choix == 1:
        if postiondeR < ordredeR:
            valeur = (mu * valeurdeI * postiondeR) / (2 * math.pi * (ordredeR) ** 2)
        else :
            valeur = (mu * valeurdeI) / (2 * math.pi * postiondeR)
    else:
        if postiondeR < ordredeR :
            valeur = 0
        else :
            valeur = (mu * valeurdeI) / (2 * math.pi * postiondeR)
    return valeur

def cham_mag(R):
    valeur = valeurdecable(R1,R,choix_R1,I1) + valeurdecable(R2,R,choix_R2,I2)
    return valeur
print('''---------------------------------------------------------
    Avec le théorème d'Ampere 
      
    La valeur de champ magnetqiue d'un point R est ''',cham_mag(R),'e\u03B8')

grap_x = range(int(R2)*3)
grap_y = [cham_mag(i) for i in grap_x]
plt.plot(grap_x,grap_y)
plt.show()

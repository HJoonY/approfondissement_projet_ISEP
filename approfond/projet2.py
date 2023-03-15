# cas On considère un câble coaxial infini cylindrique constitué (voir figure) : I
# - d’un cylindre central plein de rayon R1 parcouru par un courant d’intensité I1 uniformément réparti dans la section du cylindre
# - d’un cylindre extérieur creux de rayon R2 parcouru par un courant d’intensité I2 uniformément réparti à la surface du cylindre
# 다른 cas 도 만들기 (exercices  봐서 추가하기)

import cv2
import math
import matplotlib.pyplot as plt

fname = '/Users/Joon/Desktop/ISEP/I2/approfond/photo.png'
img = cv2.imread(fname,cv2.IMREAD_COLOR)

cv2.namedWindow('Champ magnétique d’un câble coaxial',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Champ magnétique d’un câble coaxial',100,50)

print('''

Bienvenue de simulation numerique de la Physique avec Pyton.

On considère un câble coaxial infini cylindrique constitué (voir figure) : I
- d’un cylindre central plein de rayon R1 parcouru par un courant d’intensité I1 uniformément réparti dans la section du cylindre
- d’un cylindre extérieur creux de rayon R2 parcouru par un courant d’intensité I2 uniformément réparti à la surface du cylindre

Vous pouvez inserer des chiffres de R1,R2,I1 et I2. 
Pour connaitre un valeur numerique de magnetique en un point, vous pouvez inserer. 
''')

cv2.imshow('Champ magnétique d’un câble coaxial',img)
cv2.waitKey(0)

R1 = float(input("Inserer la valeur de R1 : "))
R2 = float(input("Inserer la valeur de R2 : "))
if R2 <= R1:
    R2 = float(input("Il faut R2 etre superieur que R1 ,Inserer la valeur de R2 : "))

print("Pour avoir un câble coaxial, I1 + I2 doit etre egal à 0")
I1 = float(input("Inserer la valeur de I1 : "))
print("La valeur d'I1 ",I1,'A')
I2 = float(input("Inserer la valeur de I2 : "))
print("La valeur d'I2 ",I2,'A')
if I1 + I2 != 0 :
    I1 = float(input("Inserer la valeur de I1 : "))
    print("La valeur d'I1 ", I1, 'A')
    I2 = float(input("Inserer la valeur de I2 : "))
    print("La valeur d'I2 ", I2, 'A')

R = float(input("Inserer la valeur de R (point où vous etes ) "))

print("Avec le théorème d'Ampere")
mu = (4*math.pi)*10**(-7)
def cham_mag(R):
    if R <= R1 :
        valeur = (mu*I1*R)/(2*math.pi*(R1)**2)
        print("La valeur de magnetqiue d'un point R est ",valeur,'e\u03B8')
    elif R > R1 and R < R2 :
        valeur = (mu * I1 ) / (2 * math.pi * R )
        print("La valeur de magnetqiue d'un point R est ", valeur,'e\u03B8')
    else:
        print("La valeur de magnetqiue d'un point R est 0 e\u03B8")
        valeur = 0
    return valeur

grap_x = range(int(R)**2)
grap_y = [cham_mag(i) for i in grap_x]
plt.plot(grap_x,grap_y)
plt.show()

# 다른 cas 추가하기 
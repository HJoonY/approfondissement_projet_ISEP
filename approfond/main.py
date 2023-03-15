import tkinter
from math import *

window=tkinter.Tk()
window.title("ISEP")
window.geometry("1200x640+100+100")
window.resizable(0, 1)

label=tkinter.Label(window, text="simulation numérique de la Physique", padx = 2,pady = 1, fg="red", relief="solid")
label.pack()
welcome_text = '''

**** Bienvenue de simulation numérique de la Physique avec Pyton ****

On considère un câble coaxial infini cylindrique constitué (voir figure, et tapez l'espace) : I

Vous pouvez choisir un type de cable soit un courant I réparti dans son volume soit uniformément réparti à la surface 
 
Vous devez inserer des chiffres de R1(Rayon de cylindre interieur),R2(Rayon de cylindrique exterieur),I1(Intensité de cylindre interieur) et I2(Intensité de cylindre exterieur).
'''
label = tkinter.Label(window, text = welcome_text,justify = 'left')
label.pack()

def check():
    label.config(text= "RadioVariety_1 = " + str(RadioVariety_1.get()) + "\n" 
                       "Total = "          + str(RadioVariety_1.get() ))

RadioVariety_1=tkinter.IntVar()
RadioVariety_2=tkinter.IntVar()
type_1 = 'cable avec un courant I réparti dans son volume'
type_2 = 'un cable avec un courant I reparti dans son surface '
radio1=tkinter.Radiobutton(window, text= type_1, value=1, variable=RadioVariety_1,justify = 'left', command=check)
radio1.pack()

radio2=tkinter.Radiobutton(window, text=type_2, value=2, variable=RadioVariety_1,justify = 'left', command=check)
radio2.pack()



label=tkinter.Label(window)
label.pack()

window.mainloop()
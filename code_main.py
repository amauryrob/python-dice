#import

import random  #pour l'alétoire
import tkinter #pour créé des fenêtres
from tkinter import * 
from tkinter.ttk import *
from tkinter import Text


#tkinter

root = Tk()                                    #créé une fenêtre
root.title("Dé")                               #nom d'affichage de la fenêtre
root.geometry("500x500")                       #dimension de la fenêtre
root.resizable(width=False, height=False)      #empêcher le redimensionnement de la fenêtre

#definir les actions

a = Label (root, font=("Helvetica", 300))     #préparer la zone de texte

def roll() :
    choix = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']                     #liste de caractères spéciaux du dé
    a.config(text = f"{random.choice(choix)}")                                          #zone de résultat du lancer, ainsi que choix du dé
    a.pack(side= "top")                                                                 #faire apparaitre le lancer
                                                  

#bouton de lancer

boutton = Button(root, text = "Lancer le dé",         #créer le bouton
                          command = roll)             #action lors du clic
boutton.pack(side = "top")                            #le faire apparaitre

 

#lancer la fenêtre 

root.mainloop()

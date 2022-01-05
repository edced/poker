from random import randint


import pygame
pygame.init()

#var
couleur = 0
chiffre = 0


#couleur
while couleur == 0:
    couleur = randint(1,4)
    if couleur == 1:
        #print("coeur")
        couleur = "coeur"
    elif couleur == 2:
        #print("pique")
        couleur = "pique"
    elif couleur == 3:
        #print("carreau")
        couleur = "carreau"
    else:
        #print("treffle")
        couleur = "treffle"

while chiffre == 0:
    chiffre = randint(1,13)
    if chiffre == 1:
        #print("as")
    elif chiffre == 11:
        #print("valais")
        chiffre = "valais"
    elif chiffre == 12:
        #print("dame")
        chiffre = "dame"
    elif chiffre == 13:
        #print("roi")
        chiffre = "roi"
    else: print(chiffre)

print(chiffre, "de", couleur)

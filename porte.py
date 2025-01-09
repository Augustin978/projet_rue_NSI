# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle
from trait import trait
from couleur_aleatoire import couleur_aleatoire
from math import pi
from random import randint
# Définitions

# Fonction portes()
def portes(x,y):
    '''
    Dessine une porte de 50 pixels en largeur et 70 pixels en hauteur
    La forme du haut de la porte est aléatoirement rectangulaire ou arrondi
    La couleur pleine de remplissage est choisi aléatoirement parmi les couleurs HTML valides
    Paramètres :
        x est l'abcisse du milieu de la base de la porte
        y est l'ordonnée du sol du niveau de la porte        
    '''     

    augustin = randint(1,2)

    if augustin == 1 :
        rectangle(x,y,50,70,couleur_aleatoire())
    
    if augustin == 2 :
        rectangle(x,y,50,70,couleur_aleatoire())
        rue.fill_circle(x, y-50, 25)
        rue.stroke_arc(x,y-50,25.5, -3.3,0.1)

    
    
    
    
    
    
    
    
    
# Tests
affiche(rue)

for i in range(21) :
    portes(20+ i * 40,rue.height)
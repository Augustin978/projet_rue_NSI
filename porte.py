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
    Dessine une porte de 30 pixels en largeur et 50 pixels en hauteur
    La forme du haut de la porte est aléatoirement rectangulaire ou arrondi
    La couleur pleine de remplissage est choisi aléatoirement parmi les couleurs HTML valides
    Paramètres :
        x est l'abcisse du milieu de la base de la porte
        y est l'ordonnée du sol du niveau de la porte        
    '''     

    augustin = randint(1,2)

    if augustin == 1 :
        rue.line_width =1
        rectangle(x,y,30,50,couleur_aleatoire())
        rue.line_width = 1
    
    if augustin == 2 :
        rue.line_width = 1
        rectangle(x,y,30,35,couleur_aleatoire())
        rue.fill_circle(x, y-35, 15)
        rue.stroke_arc(x,y-35,15.5, -3.4,0.2)
        rue.line_width = 1

    
    
    
    
    
    
    
    
    
# Tests
if __name__ == '__main__':
    affiche(rue)
    portes(100,100)
    portes(200,200)

# Dépendances
from ma_rue import rue, affiche
from facade import facade
from porte import portes
from fenetre import fenetre
from random import randint ,choice
# Définitions

# Fonction rdc()
def rdc(x, couleur):
    '''
    Dessine le rdc sur une facade au niveau do sol de la rue
    avec une seule porte et 2 fenêtres placées aléatoirement.
    Paramètres
        x : abscisse du milieu de la base du RDC
        couleur : couleur fixée par l'immeuble
    '''
    # Dessine la facade
    facade()
    facade(x,couleur,0)
    # Choix d'une distribution
    ordres = ''
    randint(1,3)

    if randint == 1 :
        ordres = 'pff'
    if randint == 2 :
        ordres = 'fpf'
    if randint == 3 :
        ordres = 'ffp'
    
    if ordres[0] == 'p':
        portes(x-42.5,rue.height)
    if ordres[0] == 'f':
        fenetre(x-42.5,rue.height-20)
    if ordres[1] == 'p':
        portes(x,rue.height)
    if ordres[1] == 'f' :
        fenetre(x,rue.height-20)
    if ordres[2] == 'p':
        portes(x+42.5,rue.height)
    if ordres[2] == 'f':
        fenetre(x+42.5,rue.height-20)

    
    
    
    
        # dessiner une porte
    
    
        # dessiner une fenetre
            
    
# Tests
from couleur_aleatoire import couleur_aleatoire
affiche(rue)
for i in range(7) :
    rdc(i*160,couleur_aleatoire())
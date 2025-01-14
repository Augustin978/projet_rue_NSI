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
    facade(x,rue.height,couleur)
    # Choix d'une distribution
    
    
    
    
    
    
        # dessiner une porte
    
    
        # dessiner une fenetre
            
    
# Tests
from couleur_aleatoire import couleur_aleatoire
affiche(rue)
for i in range(7) :
    rdc(i*160, couleur_aleatoire())
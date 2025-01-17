# Dépendances

from sol import sol
from immeuble import *


# Définitions


def rue_finale(canvas):
    
    # Affichage de ma rue
    affiche(canvas)
    
    la=100
    # Dessin des immeubles
    for i  in range (4) :
        immeuble(la)
        la+=200

    
        
    # Dessin du sol de la rue
    sol()
    

# Tests
if __name__ == '__main__':
    rue_finale(rue)
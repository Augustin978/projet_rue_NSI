# Dépendances
from ma_rue import rue, affiche 
from trait import trait 

# Définitions

# Fonction sol()
def sol():
    '''
    Trace une ligne horizontale au niveau du sol de la rue
    d'épaisseur 3 pixels et de longueur 760 pixels
    centrée dans le canvas
            
    '''
    y_sol = rue.height-1 # ordonnée du sol de la rue
    trait(20,y_sol,780,y_sol,3)

    # Tests
if __name__ == '__main__':
    affiche(rue)
    sol()
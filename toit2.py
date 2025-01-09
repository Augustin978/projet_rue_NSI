# Dépendances
from ma_rue import rue, affiche
from trait import trait
# Définitions

# Fonction toit2()

def toit2(x, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    '''
    y = rue.height - niveau * 60 # ordonnée de la base du toit
   
    # trait horizontal
    trait(x,y,x+80,y)
    trait(x,y,x-80,y)
    
    
    
    
    
# Tests
affiche(rue)
for n in range(6) :
    etage(rue.width/2,couleur,n)
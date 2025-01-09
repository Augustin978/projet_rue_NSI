# Dépendances
from ma_rue import rue, affiche
from random import randint
from toit1 import toit1
from toit2 import toit2
# Définitions

# Fonction toits()

def toit(x, niveau):
    '''
    Dessine aléatoirement un toit plat ou un toit en pointe
    à l'ordonnée du niveau passé en paramètre
    Paramètres
        x : abscisse du centre de l'étage
        y_sol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    y = rue.height - niveau * 60 # ordonnée de la base du toit
    oscar=randint(1,2)
    if oscar == 1 :
        toit1(x,y)
    if oscar == 2 :
        toit2(x,y)

    
        
    
    
    
# Tests
affiche(rue)
for i in range(5) :
    for j in range(6) :
        toit(0 + 200 * i, j)
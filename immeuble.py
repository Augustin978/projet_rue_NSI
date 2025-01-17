# Dépendances
from ma_rue import rue, affiche
from couleur_aleatoire import couleur_aleatoire
from rdc import rdc
from etage import etage
from toits import toit

from random import randint

# Définitions

def immeuble(x):
    '''
    Dessine un immeuble selon les règles urbanistiques imposées
    
    Paramètres
        x : abscisse du milieu de la base de l'immeuble
        
    '''
    
     # Dessin des étages
    couleur = couleur_aleatoire()
    nombre= randint(1,5)
    for n in range(nombre) :
        etage(x,couleur,n)
    
    #Couleur facade (aléatoire)
    
    
    # Dessin du RDC
    rdc(x,couleur)
    
    

    # Dessin du toit
    toit(x,nombre)
    

# Tests
if __name__ == '__main__':
    affiche(rue)
    immeuble(rue.width/3)
    immeuble(2*rue.width/3)
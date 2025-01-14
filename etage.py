# Dépendances
from ma_rue import rue, affiche
from facade import facade
from fenetre import fenetre
from balcon import balcon 

from random import randint ,choice


# Définitions

# Fonction etage()
def etage(x, couleur, niveau):
    

    '''
    Dessine sur une facade un étage avec 3 éléments choisis aléatoirement
    parmi une fenêtre ou une porte fenêtre avec balcon.  
    
    Paramètres
        x : abscisse du milieu de la base de l'étage
        couleur : couleur fixée par l'immeuble
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    y = rue.height - niveau * 60 # ordonnée de la base de l'etage
    facade(x,couleur, niveau)
    ordre = ''
    # Murs
    
    
    for i in range (3):
        ordre+=choice('bf')

    
    if ordre[0] == 'b':
        balcon(x-42.5,y)
    if ordre[0] == 'f':
        fenetre(x-42.5,y-20)
    if ordre[1] == 'b':
        balcon(x,y)
    if ordre[1] == 'f' :
        fenetre(x,y-20)
    if ordre[2] == 'b':
        balcon(x+42.5,y)
    if ordre[2] == 'f':
        fenetre(x+42.5,y-20)

          

    
    # Eléments



    # Tests
from couleur_aleatoire import couleur_aleatoire
affiche(rue)
couleur = couleur_aleatoire()
for n in range(6) :
    etage(rue.width/2,couleur,n)
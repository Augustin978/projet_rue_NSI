# Dépendance
from ipycanvas import Canvas 



# Définition 

# Création d'un canvas nommé rue de 800 pixels de large par 400 pixels de haut
rue = Canvas(width = 800, height = 400)

# Définition d'une fonction d'affichage

def affiche(rue) :
    '''
    Efface et affiche le canvas dans le notebook
    '''
    rue.clear()
    display(rue)



# Test

# Affichage du canvas rue pour un test
affiche(rue)
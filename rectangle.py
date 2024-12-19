# Dépendance
from ma_rue import rue, affiche

# Définitions

# Fonction rectangle()
def rectangle(x,y,w,h,c):
    x = x - w/2
    y = y - h


    '''
    Dessine un rectangle avec un contour noir et rempli de la couleur passée en paramètre
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
        c : couleur du remplissage
    '''
    # rectangle
    rue.fill_style = c 
    rue.fill_rect(x, y, w, h)
    

    # contour rectangle
    rue.stroke_style = 'black'
    rue.stroke_rect(x, y, w, h)
    
    
    
    
    
    
# Tests
affiche(rue)
rectangle(0, 50,200,100,'YellowGreen')
rectangle(800, 450,200,100,'plum')
rectangle(400, 250,200,100,'SkyBlue')
rectangle(400, 250,100,50,'salmon')
# Autres tests
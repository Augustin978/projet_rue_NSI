from ma_rue import rue, affiche
# Définitions

# Fonction trait()
def trait(x1,y1,x2,y2,w=1):
    '''
    dessine un trait entre les 2 points transmis en paramètres
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    
    '''
    
    rue.line_width = w 
    rue.stroke_line(x1, y1, x2, y2)
    rue.line_width = 1 
    
    
# Tests
if __name__ == '__main__':
    affiche(rue)
    trait(50, 25, rue.width/2, rue.height/2)
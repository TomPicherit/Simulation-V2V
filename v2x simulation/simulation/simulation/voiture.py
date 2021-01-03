import turtle

# Creation de notre classe Voiture
class Voiture:
    def __init__(self,coord_x,coord_y):
     
        # Initialisation du module turtle pour notre joueur
        self.pad = turtle.Turtle()
        self.pad.speed(0)
        self.pad.color("white")
        self.pad.hideturtle()
        
        self.vitesse = 0
        self.acceleration = 1
        self.y = coord_y
        self.x = coord_x
       

    # Affichage de la voiture a l'ecran
    def affiche(self):
        self.pad.up() 
        self.pad.goto( self.x, self.y)                       
        self.pad.down()
        self.pad.begin_fill()  
        for i in range(2): 
            self.pad.forward(50) #avance
            self.pad.left(90)     #angle
            self.pad.forward(10) 
            self.pad.left(90)
        self.pad.end_fill()
        

    def move_right(self):
        if self.x < 590:  
            self.x += (self.vitesse)*(self.acceleration)
        else:
            self.vitesse = 0
        self.pad.clear()
        self.affiche()
        
    
    def arret(self):
        self.vitesse = 0
        
        


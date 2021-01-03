# -*- coding: utf-8 -*-
import turtle
from voiture import Voiture
import time

# Creation de notre classe game
class Simu():
    def __init__(self):
        
        # Initialisation de notre fenetre
        self.ecran = turtle.Screen()
        self.ecran.title("Pong")  
        self.ecran.bgcolor("black")   
        self.ecran.setup(1280, 720)       
        self.ecran.tracer(0)
        
        # Initialisation de l'affichage des vitesses
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square") 
        self.pen.color("white")
        self.pen.hideturtle() 
        self.pen.penup() 
        self.pen.hideturtle() 
        self.pen.goto(0, 200)
        
        # Initialisation de l'affichage de la simulation
        self.pen1 = turtle.Turtle()
        self.pen1.speed(0)
        self.pen1.shape("square") 
        self.pen1.color("white")
        self.pen1.hideturtle() 
        self.pen1.penup() 
        self.pen1.hideturtle() 
        self.pen1.goto(-600, 300)
        
        # Initialisation de l'affichage du chrono
        self.pen2 = turtle.Turtle()
        self.pen2.speed(0)
        self.pen2.shape("square") 
        self.pen2.color("white")
        self.pen2.hideturtle() 
        self.pen2.penup() 
        self.pen2.hideturtle() 
        self.pen2.goto(-600, 300)
        
        #g�n�ration des joueurs
        self.voiture_a = Voiture(-450,50)
        self.voiture_b = Voiture(-50,50)
        
        self.voiture_c = Voiture(-450,-50)
        self.voiture_d = Voiture(0,-50)
        
        # Objet du chronometre
        self.debut = 0
        self.chrono = 0
        
        # Objet de la simulation
        self.simu = 0
    

    # Lancement simulation 1
    def simu_1(self):
        self.simu = 1
        self.debut = time.time()
        self.voiture_a.vitesse = 90/100
        self.voiture_b.vitesse = 40/100
        
    # Lancement simulation 2
    def simu_2(self):
        self.simu = 2
        self.debut = time.time()
        self.voiture_c.vitesse = 70/100
        self.voiture_d.vitesse = 50/100
    
    # Affichage d'un chrnomètre
    def chronometre(self):
        if self.simu != 0:
            self.pen2.clear()
            self.chrono = (time.time() - self.debut)
            self.pen2.write("Chrono : {}".format(round(self.chrono,1)), align="left", font=("Arial", 18, "normal"))
        else:
            self.pen2.clear()
            self.pen2.write("Chrono : {}".format(self.chrono), align="left", font=("Arial", 18, "normal"))
   
    # Affichage des vitesses en temps reel
    def affiche_vitesse(self):
        if self.simu == 1:
            self.pen.clear()
            self.pen.write("Voiture A: {} km/h  Voiture B: {} km/h".format(round(self.voiture_a.vitesse*100,2), round(self.voiture_b.vitesse*100,2)), align="center", font=("Arial", 18, "normal"))
        
        elif self.simu == 2:
            self.pen.clear()
            self.pen.write("Voiture C: {} km/h  Voiture D: {} km/h".format(round(self.voiture_c.vitesse*100,2), round(self.voiture_d.vitesse*100,2)), align="center", font=("Arial", 18, "normal"))
        
        elif self.simu == 10:
            self.pen.clear()
            self.pen.write("Crash : la voiture A ne s'est pas arrêtée à temps".format(), align="center", font=("Arial", 18, "normal"))
        
        else:
            self.pen.clear()
            self.pen.write("Tapez 1 ou 2 pour lancer une simulation".format(), align="center", font=("Arial", 18, "normal"))
    
    def reset(self):
        
        self.voiture_a.x = -450
        self.voiture_b.x = -50
        
        self.voiture_a.pad.clear
        self.voiture_b.pad.clear
        self.voiture_c.pad.clear
        self.voiture_d.pad.clear
        
        self.voiture_a.affiche()
        self.voiture_b.affiche()
        self.voiture_c.affiche()
        self.voiture_d.affiche() 
        
        self.simu = 0
        
        self.debut = 0
        self.chrono = 0
    
#    def deceleration(self):
#        self.vitesse -= 0.05
##    def latence(self):
##        self.temps+= self.chrono
##        if self.chrono != tps
#        
        
        
        
        
        
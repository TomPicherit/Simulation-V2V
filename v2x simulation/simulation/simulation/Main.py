# -*- coding: utf-8 -*-

#modifier pour que la voiture soit verte que quand y a latence
#modifier pour que la voiture reparte une fois qu'elle ralentie


import turtle
from simu import Simu


# Chargement du jeu
simulation = Simu()

running = True

# Initialisation de l'affichage
simulation.voiture_a.affiche()
simulation.voiture_b.affiche()
simulation.voiture_c.affiche()
simulation.voiture_d.affiche() 

#Parametres en fonction de la simmulation
#Echelle : 1px equivaut a 0.5m et 1 en vitesse equivaut a 100km/h
#distance entre deux voiture mini pour eviter accident
distance_secu = 100

distance_visible = 50+300

turtle.Screen().onkey(simulation.reset,"r")
turtle.Screen().onkey(simulation.voiture_b.arret,"a")
turtle.Screen().onkey(simulation.simu_1,"1")
turtle.Screen().onkey(simulation.simu_2,"2")
#turtle.Screen().onkey(pong.voiture_a.arret,"a")
turtle.Screen().listen()

# Boucle du jeu
while running:
    
    # Mise a jour de l'affichage
    simulation.ecran.update()
    
    # Affiche le chrono
    simulation.chronometre()
    
    # Affiche la vitesse
    simulation.affiche_vitesse()
    
    # Cas de la simu 1
    if simulation.simu == 1:
        
        #♦ SI la voiture voit celle de devant, aucun danger
        if simulation.voiture_a.x > simulation.voiture_b.x-distance_visible and simulation.voiture_a.x+25 < simulation.voiture_b.x-25-distance_secu:
            
            simulation.voiture_a.pad.color("green")
        
        # Si on veut freiner (latence)
        elif simulation.voiture_a.x+25 > simulation.voiture_b.x-25-distance_secu and simulation.voiture_a.x+25 < simulation.voiture_b.x-25-distance_secu/2:

            simulation.voiture_a.pad.color("orange")
        
        # Si on freine enfin et pas de collision
        elif simulation.voiture_a.x+25 > simulation.voiture_b.x-25-distance_secu/2 and simulation.voiture_a.x+25 < simulation.voiture_b.x-25:
            
            simulation.voiture_a.pad.color("red")
            
            # Si la voiture de devant est arretee : frein d'arret de panique
            if simulation.voiture_b.vitesse == 0:
                # Si la voiture de derriere avance encore
                if  simulation.voiture_a.vitesse >= 0.002:
                        simulation.voiture_a.vitesse -= 0.002
                else:
                    simulation.voiture_a.vitesse = 0
                    
            # Sinon on ralentit
            else:
                if  simulation.voiture_a.vitesse > simulation.voiture_b.vitesse-0.1:
                    simulation.voiture_a.vitesse -= 0.001  
        # Crash
        elif simulation.voiture_a.x+25 >= simulation.voiture_b.x-25:
            simulation.voiture_a.vitesse = 0
            simulation.voiture_b.vitesse = 0
            simulation.voiture_a.pad.color("yellow")
            
        simulation.voiture_a.move_right()
        simulation.voiture_b.move_right()

    # Cas de la simu 2
    if simulation.simu == 2:
                
        # Si on est trop proche de la voiture de devant
        if simulation.voiture_c.x+25 > simulation.voiture_d.x-distance_secu:
            
            # Si la voiture de devant est arretee
            if simulation.voiture_d.vitesse == 0:
                simulation.voiture_c.vitesse = 0
            # Sinon on prend la meme allure que la voiture de devant
            else:
                simulation.voiture_c.vitesse = simulation.voiture_d.vitesse
        
        simulation.voiture_c.move_right()
        simulation.voiture_d.move_right()






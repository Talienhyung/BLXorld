from Programme.classBouton import *
from Programme.classImage import *
from Programme.fonctionText import *
from Programme.conv import *
import pygame
pygame.init()



btn1= Boutons(conv(1000,410),"Image/Assert/btn/btnchoix1.png","centre")
btn1.resize(conv2(btn1.image.get_width(),btn1.image.get_height()))
btn2= Boutons(conv(1000,720),"Image/Assert/btn/btnchoix1.png","centre")
btn2.resize(conv2(btn2.image.get_width(),btn2.image.get_height()))
btn3= Boutons(conv(1000,909),"Image/Assert/btn/btnchoix1.png","centre")
btn3.resize(conv2(btn3.image.get_width(),btn3.image.get_height()))
btn4= Boutons(conv(1000,615),"Image/Assert/btn/btnchoix1.png","centre")
btn4.resize(conv2(btn4.image.get_width(),btn4.image.get_height()))
btn5= Boutons(conv(1000,321),"Image/Assert/btn/btnchoix1.png","centre")
btn5.resize(conv2(btn5.image.get_width(),btn5.image.get_height()))



def faire_un_choix(fonds, texte1, texte2, texte3, nombre, liste, game_state):
    while nombre == 2 :
        pygame.display.flip()
        surface.fill(0)
        fermer_le_jeu(game_state)
        fonds.draw(surface, (l,0))
        doublechoix(surface)
        text_de_choix(surface, texte1, conv(1000,410))
        text_de_choix(surface, texte2, conv(1000,720))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sauvegarde(game_state)
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if btn1.positionCentre().collidepoint(event.pos):
                        choix=liste[0]
                        nombre =1
                    elif btn2.positionCentre().collidepoint(event.pos):
                        choix=liste[1]
                        nombre =1
                    elif croix.positionTopLeft().collidepoint(event.pos):
                        pygame.quit()
                        quit()
    
    while nombre == 3 :
        pygame.display.flip()
        surface.fill(0)
        fermer_le_jeu(game_state)
        fonds.draw(surface, (l,0))
        triplechoix(surface)
        text_de_choix(surface, texte1, conv(1000,909))
        text_de_choix(surface, texte2, conv(1000,615))
        text_de_choix(surface, texte3, conv(1000,321))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sauvegarde(game_state)
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if btn3.positionCentre().collidepoint(event.pos):
                        choix=liste[0]
                        nombre =1
                    elif btn4.positionCentre().collidepoint(event.pos):
                        choix=liste[1]
                        nombre =1
                    elif btn5.positionCentre().collidepoint(event.pos):
                        choix=liste[2]
                        nombre =1
                    elif croix.positionTopLeft().collidepoint(event.pos):
                        pygame.quit()
                        quit()
    
    return choix 





def doublechoix(surface):
    btn1.doubleAffichageBouton("Image/Assert/btn/btnchoix1.png","Image/Assert/btn/btnchoix2.png", surface)
    btn2.doubleAffichageBouton("Image/Assert/btn/btnchoix1.png","Image/Assert/btn/btnchoix2.png", surface) 

def triplechoix(surface):
    btn3.doubleAffichageBouton("Image/Assert/btn/btnchoix1.png","Image/Assert/btn/btnchoix2.png", surface)
    btn4.doubleAffichageBouton("Image/Assert/btn/btnchoix1.png","Image/Assert/btn/btnchoix2.png", surface)
    btn5.doubleAffichageBouton("Image/Assert/btn/btnchoix1.png","Image/Assert/btn/btnchoix2.png", surface) 
    

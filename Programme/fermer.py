from Programme.fonctionAffichage import *
from Programme.classBouton import *
from Sauvegarde.sauvegarde import *
import pygame 
pygame.init()


def fermer_le_jeu(game_state):
	CroixAffichage()
	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sauvegarde(game_state)
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if croix.positionTopLeft().collidepoint(event.pos):
                        sauvegarde(game_state)
                        pygame.quit()
                        quit()

def mapAccess(a):
    e=1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if a.positionCentre().collidepoint(event.pos):
                    e=2
    return e
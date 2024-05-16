import pygame
pygame.init()
from Programme.classBouton import *


ecran = pygame.display.Info()
largeur, hauteur = ecran.current_w, ecran.current_h
surface = pygame.display.set_mode((largeur, hauteur), pygame.FULLSCREEN)
croix= Boutons((largeur-largeur/40, 0),'Image/Assert/btn/croix1.png', "topleft")
croix.resize((largeur/40, (croix.image.get_height()*largeur/40)//croix.image.get_width()))

def widthEcran():
    return largeur

def heightEcran():
    return hauteur


def PremierAffichage(image):
    largeur2=(image.get_width()*hauteur)//image.get_height()
    start= pygame.transform.scale(image, (largeur2, hauteur))
    l= (largeur-largeur2)//2
    surface.fill(0)
    surface.blit(start,(l,0))
    # return start, surface, l, (largeur, hauteur)


def Choper_le_centre(image):
    largeur2=(image.get_width()*hauteur)//image.get_height()
    start= pygame.transform.scale(image, (largeur2, hauteur))
    l= (largeur-largeur2)//2
    return l, largeur2



def CroixAffichage():
    surface.blit(croix.image, croix.positionTopLeft())
    if croix.colli():
        croix.changeImage('Image/Assert/btn/croix2.png')
    else:
        croix.changeImage('Image/Assert/btn/croix1.png')
    
    
    

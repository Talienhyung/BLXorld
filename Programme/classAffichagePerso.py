import pygame, sys
from pygame.locals import *
from Programme.conv import *
pygame.init()


class Perso:
    def __init__(self,x, sprite, width, height, centre):
        self.centre=centre
        self.perso = pygame.image.load(sprite)
        self.dimmention = [width, height]
        self.image=[]
        self.index=x
        self.index1 = x
        self.nom = "???"
        for x in range(0,self.index*width, height):   
            self.image.append(self.perso.subsurface(x,0,width,height))
        
    def positionCentre(self, x):
        self.rect=self.image[x].get_rect()
        self.rect.center=self.centre
        return self.rect


    def changenom(self, newNom):
        self.nom = newNom


    def resize(self, width, height):
            self.perso = pygame.transform.scale(self.perso, (self.index*width, height))
            for x in range(0,self.index*width, height):   
                self.image.append(self.perso.subsurface(x,0,width,height))


    def affiche(self, fenetre, index):
        fenetre.blit(self.image[index], self.positionCentre(index))

    def bouge_personnage(self,fenetre):
        self.index1 += 1
        if self.index1 >= len(self.image):
            self.index1=0
        self.affiche(fenetre, self.index)

    def NewNom(self, NewNom):
        self.nom=NewNom


    
al= Perso(16, "Image/SpritePerso/AL.png", 600, 600, conv(1000,720))
al.resize(800, 800)

victoria= Perso(17, "Image/SpritePerso/Victoria.png", 600, 600, conv(1000,720))
victoria.resize(800, 800)

utilisateur = Perso(14, "Image/SpritePerso/utilisateur.png", 600, 600, conv(1000,720))
utilisateur.resize(800, 800)

john= Perso(17, "Image/SpritePerso/John.png", 600, 600, conv(1000,720))
john.resize(800, 800)

LaBoulangere= Perso(10, "Image/SpritePerso/La_Boulangere.png", 602,602, conv(1000,720))
LaBoulangere.resize(802, 802)

scene_perso_avancement=[0,0,0,0,0] # Al, Victoria, John, La boulangere, Train
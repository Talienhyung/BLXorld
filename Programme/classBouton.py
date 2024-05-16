import pygame, sys
from pygame.locals import *
from Programme.conv import *
pygame.init()



class Boutons:
    def __init__(self,centre, image, pos):
        self.centre=centre
        self.image1= image
        self.image=pygame.image.load(image)
        self.pos=pos
    
    def positionCentre(self):
        self.rect=self.image.get_rect()
        self.rect.center=self.centre
        return self.rect

    def resize(self, dimention):
            self.dimention = dimention
            self.image = pygame.transform.scale(self.image, dimention)
            return self.image

    def changeImage(self, Newimage):
        self.image=pygame.image.load(Newimage)
        self.image=self.resize(self.dimention)
        
        
    def positionTopLeft(self):
        self.rect=self.image.get_rect()
        self.rect.topleft=self.centre
        return self.rect
    
    def colli(self):
        if self.pos=="centre":
            if self.positionCentre().collidepoint(pygame.mouse.get_pos()):
                return True
        else: 
            if self.positionTopLeft().collidepoint(pygame.mouse.get_pos()):
                return True

    def AffichageBouton(self, surface):
        if self.pos=="centre":
            surface.blit(self.image, self.positionCentre())
        else: surface.blit(self.image,self.positionTopLeft())


    def doubleAffichageBouton(self, image1, image2,surface):
        if self.pos=="centre":
            surface.blit(self.image, self.positionCentre())
        else: surface.blit(self.image,self.positionTopLeft())
        if self.colli():
            self.changeImage(image2)
        else: self.changeImage(image1)
        


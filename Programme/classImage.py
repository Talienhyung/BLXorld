import pygame, sys
from pygame.locals import *
from Programme.classBouton import Boutons
from Programme.conv import *
pygame.init()

class Image:
    def __init__(self, filename):
        self.original_image =pygame.image.load(filename)
        self.rect = self.original_image.get_rect()

    def resize(self, dim):
        self.image = pygame.transform.scale(self.original_image, dim)
        self.dim=dim
        return self.image

    def changeImage(self, new):
        self.image= pygame.image.load(new)
        self.image=self.resize(self.dim)

    def draw(self, surface, whr):
        surface.blit(self.image, whr)

    

bulle=Image("Image/Assert/btn/bulleDialogue.png")
bulle.resize(conv2(bulle.original_image.get_width(),bulle.original_image.get_height()))

MaisonVoisinExterieur1=Image("Image/Fond/MaisonVoisinExterieur.png")
MaisonVoisinExterieur1.resize(conv2(MaisonVoisinExterieur1.original_image.get_width(),MaisonVoisinExterieur1.original_image.get_height()))
MaisonVoisinExterieur2=Image("Image/Fond/MaisonVoisinExterieur2.png")
MaisonVoisinExterieur2.resize(conv2(MaisonVoisinExterieur2.original_image.get_width(),MaisonVoisinExterieur2.original_image.get_height()))
maisonVoisinInterieur=Image("Image/Fond/MaisonVoisinInterieur.png")
maisonVoisinInterieur.resize(conv2(maisonVoisinInterieur.original_image.get_width(),maisonVoisinInterieur.original_image.get_height()))
Librairie=Image("Image/Fond/Librairie.png")
Librairie.resize(conv2(Librairie.original_image.get_width(),Librairie.original_image.get_height()))
Librairie2=Image("Image/Fond/Librairie2.png")
Librairie2.resize(conv2(Librairie2.original_image.get_width(),Librairie2.original_image.get_height()))
Librairie3=Image("Image/Fond/Librairie3.png")
Librairie3.resize(conv2(Librairie3.original_image.get_width(),Librairie3.original_image.get_height()))
Parc1=Image("Image/Fond/Parc.png")
Parc1.resize(conv2(Parc1.original_image.get_width(),Parc1.original_image.get_height()))
Parc2=Image("Image/Fond/Parc2.png")
Parc2.resize(conv2(Parc2.original_image.get_width(),Parc2.original_image.get_height()))
# Eglise=Image("Image/Fond/Eglise.png")
# Eglise.resize(conv2(Eglise.original_image.get_width(),Eglise.original_image.get_height()))
Boulangerie1=Image("Image/Fond/Boulangerie.png")
Boulangerie1.resize(conv2(Boulangerie1.original_image.get_width(),Boulangerie1.original_image.get_height()))
Boulangerie2=Image("Image/Fond/Boulangerie2.png")
Boulangerie2.resize(conv2(Boulangerie2.original_image.get_width(),Boulangerie2.original_image.get_height()))
Boulangerie3=Image("Image/Fond/Boulangerie3.png")
Boulangerie3.resize(conv2(Boulangerie3.original_image.get_width(),Boulangerie3.original_image.get_height()))
Temple=Image("Image/Fond/Temple.png")
Temple.resize(conv2(Temple.original_image.get_width(),Temple.original_image.get_height()))
Synagogue=Image("Image/Fond/Synagogue.png")
Synagogue.resize(conv2(Synagogue.original_image.get_width(),Synagogue.original_image.get_height()))
Mosquée=Image("Image/Fond/Mosquée.png")
Mosquée.resize(conv2(Mosquée.original_image.get_width(),Mosquée.original_image.get_height()))
Mairie=Image("Image/Fond/Mairie.png")
Mairie.resize(conv2(Mairie.original_image.get_width(),Mairie.original_image.get_height()))
Hopital=Image("Image/Fond/Hôpital.png")
Hopital.resize(conv2(Hopital.original_image.get_width(),Hopital.original_image.get_height()))
Gare=Image("Image/Fond/Gare.png")
Gare.resize(conv2(Gare.original_image.get_width(),Gare.original_image.get_height()))
Ecole=Image("Image/Fond/Ecole.png")
Ecole.resize(conv2(Ecole.original_image.get_width(),Ecole.original_image.get_height()))
Cinema=Image("Image/Fond/Cinéma.png")
Cinema.resize(conv2(Cinema.original_image.get_width(),Cinema.original_image.get_height()))
Cafe=Image("Image/Fond/Café.png")
Cafe.resize(conv2(Cafe.original_image.get_width(),Cafe.original_image.get_height()))
Bibliotheque=Image("Image/Fond/Bibliothèque.png")
Bibliotheque.resize(conv2(Bibliotheque.original_image.get_width(),Bibliotheque.original_image.get_height()))
Bar=Image("Image/Fond/Bar.png")
Bar.resize(conv2(Bar.original_image.get_width(),Bar.original_image.get_height()))







import pygame

class Musique :
    def __init__(self, fichier):
         
        self.son = pygame.mixer.Sound(fichier)

    def jouer(self):
        self.son.play()

musique = Musique("Musique/musique_start.mp3")
from Programme.fonctionText import *
import pygame

pygame.init()
EcranNom= pygame.image.load('Image/Assert\Accuille\EcranNom.png')

def nom(game_state):
    fini = False
    nom = ""
    while not fini:
        pygame.display.flip()
        sauvegarde(game_state)
        surface.fill(0)
        PremierAffichage(EcranNom)
        CroixAffichage()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fini = True
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and len(nom) < 10:
                    nom += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    nom = nom[:-1]
                elif event.key == pygame.K_RETURN:
                    fini = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    fini = True

        


        # Afficher le nom entré par l'utilisateur
        text_de_choix(surface, nom, conv(1000,947))

        # Mettre à jour l'écran
        pygame.display.flip()

    # Enregistrer le nom
    utilisateur.nom=nom


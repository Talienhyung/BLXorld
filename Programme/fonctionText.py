import pygame
from Programme.conv import *
from Programme.fermer import *
from Programme.classImage import *
from Programme.classAffichagePerso import *

pygame.init()
font = pygame.font.Font("Police/GlacialIndifference-Regular.otf", 50)
font2 = pygame.font.Font("Police/GlacialIndifference-Regular.otf", 30)
font3 = pygame.font.Font("Police/GlacialIndifference-Regular.otf", 40)

r=0
p=1000

def text_de_nom(surface, texte, centre):
    text_surface = font3.render(texte, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = centre
    surface.blit(text_surface, text_rect)


def afficher_texte(surface, texte,game_state):
    if r==0:
        surface_texte = font.render(texte, True, (255, 255, 255))
        x = surface.get_width() // 2 - surface_texte.get_width() // 2
        y = surface.get_height() // 2 - surface_texte.get_height() // 2
        surface.fill((0, 0, 0))
        fermer_le_jeu(game_state)
        surface.blit(surface_texte, (x, y))
        pygame.display.flip()
        pygame.time.wait(p), fermer_le_jeu(game_state)
        


    elif r==1:
        for i in range(len(texte)):
            # Affiche une lettre supplémentaire du texte
            texte_affiche = texte[:i+1]
            surface_texte = font.render(texte_affiche, True, (255, 255, 255))
            x = surface.get_width() // 2 - surface_texte.get_width() // 2
            y = surface.get_height() // 2 - surface_texte.get_height() // 2
            surface.fill((0, 0, 0))
            fermer_le_jeu(game_state)
            surface.blit(surface_texte, (x, y))
            pygame.display.flip()

            # Attend un court instant
            pygame.time.wait(50), fermer_le_jeu(game_state)


def afficher_texte_dialogue(surface, texte, obj, perso, index,game_state):
    if r==0:
        surface_texte = font2.render(texte, True, (0, 0, 0))
        surface.fill(0)
        fermer_le_jeu(game_state)
        obj.draw(surface, (l,0))
        perso.affiche(surface,index)
        bulle.draw(surface, (l,0))
        text_de_nom(surface, perso.nom, conv(268,1102))
        surface.blit(surface_texte, conv(55,1212))
        pygame.display.flip()
        pygame.time.wait(p), fermer_le_jeu(game_state)

    elif r==1:
        for i in range(len(texte)):
            # Affiche une lettre supplémentaire du texte
            texte_affiche = texte[:i+1]
            surface_texte = font2.render(texte_affiche, True, (0, 0, 0))
            surface.fill(0)
            fermer_le_jeu(game_state)
            obj.draw(surface, (l,0))
            perso.affiche(surface,index)
            bulle.draw(surface, (l,0))
            text_de_nom(surface, perso.nom, conv(268,1102))
            surface.blit(surface_texte, conv(55,1212))
            pygame.display.flip()

            # Attend un court instant
            pygame.time.wait(0), fermer_le_jeu(game_state)

def text_de_choix(surface, texte, centre):
    text_surface = font3.render(texte, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = centre
    surface.blit(text_surface, text_rect)

def afficher_texte_dialogue_utilisateur(surface, texte, obj, perso, index,game_state):
    if r==0:
        surface_texte = font2.render(texte, True, (0, 0, 0))
        surface.fill(0)
        fermer_le_jeu(game_state)
        obj.draw(surface, (l,0))
        perso.affiche(surface,index)
        bulle.draw(surface, (l,0))
        text_de_nom(surface, utilisateur.nom, conv(268,1102))
        surface.blit(surface_texte, conv(55,1212))
        pygame.display.flip()
        pygame.time.wait(p), fermer_le_jeu(game_state)

    elif  r== 1:
        for i in range(len(texte)):
            # Affiche une lettre supplémentaire du texte
            texte_affiche = texte[:i+1]
            surface_texte = font2.render(texte_affiche, True, (0, 0, 0))
            surface.fill(0)
            fermer_le_jeu(game_state)
            obj.draw(surface, (l,0))
            perso.affiche(surface,index)
            bulle.draw(surface, (l,0))
            text_de_nom(surface, utilisateur.nom, conv(268,1102))
            
            surface.blit(surface_texte, conv(55,1212))
            pygame.display.flip()

            # Attend un court instant
            pygame.time.wait(1), fermer_le_jeu(game_state)



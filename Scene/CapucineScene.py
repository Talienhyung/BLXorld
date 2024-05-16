from Programme.choix import *
from Programme.fonctionText import *
from Programme.classPronom import *

n=100

def testBar(game_state):
    afficher_texte_dialogue_utilisateur(surface, "Patateverte", Bar, utilisateur, 3, game_state)
    pygame.time.wait(n)

def testBibliotheque(Brochure, game_state):
    afficher_texte_dialogue_utilisateur(surface, "Patateverte", Bibliotheque, utilisateur, 3, game_state)
    pygame.time.wait(n)

def testEcole(game_state):
    afficher_texte_dialogue_utilisateur(surface, "Patateverte", Ecole, utilisateur, 3, game_state)
    pygame.time.wait(n)

# def testMagasin(game_state):
#     afficher_texte_dialogue_utilisateur(surface, "Patateverte", Mairie, utilisateur, 3, game_state)
#     pygame.time.wait(n)

def testMairie(game_state):
    afficher_texte_dialogue_utilisateur(surface, "Patateverte", Mairie, utilisateur, 3, game_state)
    pygame.time.wait(n)


def testCafé(game_state):
    afficher_texte_dialogue_utilisateur(surface, "Patateverte", Cafe, utilisateur, 3, game_state)
    pygame.time.wait(n)


def testCinema(game_state):
    afficher_texte_dialogue_utilisateur(surface, "Patateverte", Cinema, utilisateur, 3, game_state)
    pygame.time.wait(n)


def testMagasin(Montre, game_state):
    afficher_texte_dialogue_utilisateur(surface, "Patateverte", Cinema, utilisateur, 3, game_state)
    pygame.time.wait(n)
    return "Montre"
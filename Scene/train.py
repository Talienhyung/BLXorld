from Programme.choix import *
from Programme.fonctionText import *
from Programme.classPronom import *

n=0
def train1 (game_state, destinationListe, desti, desti2, desti3, le, la, les):
    afficher_texte(surface, "Vous arrivez à la gare.", game_state)
    pygame.time.wait(n)
    if destinationListe[0]==0 and destinationListe[1]==0 and destinationListe[2]==0:
        afficher_texte(surface, "Où voulez-vous allez ? ", game_state)
        pygame.time.wait(n)
        destination = faire_un_choix(Parc1, "desti", "desti2", "desti3", 3, [["desti",[1,0,0]],["desti2",[0,1,0]],["desti3",[0,0,1]]], game_state)
        destinationListe=destination[1]
        return destination[0], destinationListe

    elif destinationListe[0]==0 and destinationListe[1]==0:
        afficher_texte(surface, "Où voulez-vous allez ? ", game_state)
        pygame.time.wait(n)
        destination = faire_un_choix(Parc1, "desti", "desti2", "", 2, [["desti",[1,0,1]],["desti2",[0,1,1]],""], game_state)
        destinationListe=destination[1]
        return destination[0], destinationListe
    
    elif destinationListe[0]==0 and destinationListe[2]==0:
        afficher_texte(surface, "Où voulez-vous allez ? ", game_state)
        pygame.time.wait(n)
        destination = faire_un_choix(Parc1, "desti", "desti3", "", 2, [["desti",[1,1,0]],["desti3",[0,1,1]],""], game_state)
        destinationListe=destination[1]
        return destination[0], destinationListe
    
    elif destinationListe[1]==0 and destinationListe[2]==0:
        afficher_texte(surface, "Où voulez-vous allez ? ", game_state)
        pygame.time.wait(n)
        destination = faire_un_choix(Parc1, "desti2", "desti3", "", 2, [["desti2",[1,1,0]],["desti3",[1,0,1]],""], game_state)
        destinationListe=destination[1]
        return destination[0], destinationListe

    else:
        if destinationListe[0]==0:
            afficher_texte(surface, "Direction "+le+ desti +" !", game_state)
            pygame.time.wait(n)
            return desti, [1,1,1]
        if destinationListe[1]==0:
            afficher_texte(surface, "Direction "+la+ desti2+" !", game_state)
            pygame.time.wait(n)
            return desti2, [1,1,1]
        if destinationListe[2]==0:
            afficher_texte(surface, "Direction "+les+ desti3+" !", game_state)
            pygame.time.wait(n)
            return desti3, [1,1,1]


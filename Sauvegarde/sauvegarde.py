# Pour sauvegarder le jeu
import json
def sauvegarde(game_state):
    with open("Sauvegarde/save_file.json", "w") as f:
        json.dump(game_state, f)

# Pour charger le jeu

def ouvrir_sauvegarde():
    with open("Sauvegarde/save_file.json", "r") as f:
        game_state = json.load(f)
    return game_state



#game_state, pronom, scene perso avancement
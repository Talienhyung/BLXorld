from Programme.choix import *
from Programme.fonctionText import *
from Programme.classPronom import *

n=0

def JohnScene1(pron, game_state):
    afficher_texte(surface, "La personne habitant à côté semble être présente,", game_state)
    pygame.time.wait(n)
    afficher_texte(surface, "vous décidez de sonner à sa porte.", game_state)
    pygame.time.wait(n)
    afficher_texte(surface, "Un homme vous ouvre.", game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue(surface, "Bonjour, vous êtes ?", MaisonVoisinExterieur1, john, 8, game_state)
    pygame.time.wait(n)
    choix = faire_un_choix(MaisonVoisinExterieur1, "Partir en courant", "Se présenter", "...", 3, [1,2,3], game_state)
    if choix == 1:
        afficher_texte_dialogue_utilisateur(surface, "...", MaisonVoisinExterieur1, utilisateur, 0, game_state)
        pygame.time.wait(n)
        afficher_texte(surface, "L'homme vous rattrape par le bras.", game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Ahah vous n'êtes pas un"+pron.e()+" cambrioleu" +pron.euse() +" j'espère..", MaisonVoisinExterieur1, john, 5, game_state)
        pygame.time.wait(n)
        choix = faire_un_choix(MaisonVoisinExterieur1, "...", "Se présenter", "", 2, [1,2], game_state)
        if choix==1:
            choix=3
        else : choix=2

    if choix == 3 :
        afficher_texte_dialogue_utilisateur(surface, "...", MaisonVoisinExterieur2, john, 7, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Ahah vous êtes timide, ne vous inquiétez pas, je ne mange pas.", MaisonVoisinExterieur1, john, 5, game_state)
        pygame.time.wait(n)
        choix = 2
    if choix == 2:
        afficher_texte_dialogue_utilisateur(surface, "Oh ! Je suis votre nouv"+ pron.eau()+ " voisin"+ pron.e()+ " !", MaisonVoisinExterieur1, john, 1, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Oh enchanté ! Vous voulez entrer ?", MaisonVoisinExterieur1, john, 5, game_state)
        pygame.time.wait(n)
        choix = faire_un_choix(MaisonVoisinExterieur1, "Accepter", "Refuser", "", 2, [1,2], game_state)
        if choix == 2:
            afficher_texte_dialogue_utilisateur(surface, "Oh, je ne reste pas, je voulais juste me présenter et vous saluer !", MaisonVoisinExterieur1, john, 6, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Et bien enchanté ! Si vous avez un quelconque problème, n'hésitez pas !", MaisonVoisinExterieur1, john, 5, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Merci beaucoup, au revoir !", MaisonVoisinExterieur1, john, 1, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Au revoir !", MaisonVoisinExterieur1, john, 0, game_state)
            pygame.time.wait(n)
        if choix== 1:
            afficher_texte_dialogue_utilisateur(surface, "Pourquoi pas !", MaisonVoisinExterieur1, john, 6, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Allez-y, rentrez !", MaisonVoisinExterieur1, john, 4, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Merci", maisonVoisinInterieur, john, 1, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Thé ou café ?", maisonVoisinInterieur, john, 4, game_state)
            pygame.time.wait(n)
            choix = faire_un_choix(maisonVoisinInterieur, "Thé", "Café", "Non merci", 3, [1,2,3], game_state)
            if choix == 1:
                afficher_texte_dialogue_utilisateur(surface, "Je veux bien un thé", maisonVoisinInterieur, john, 1, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Très bon choix ! Je vais chercher ça !", maisonVoisinInterieur, john, 4, game_state)
                pygame.time.wait(n)
                afficher_texte(surface, "L'homme vous laisse un moment seul"+ pron.e()+ " ...", game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Désolé pour l'attente !", maisonVoisinInterieur, john, 2, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Et hop, deux thés bien chauds !", maisonVoisinInterieur, john, 5, game_state)
                pygame.time.wait(n)
            if choix == 2:
                afficher_texte_dialogue_utilisateur(surface, "Je veux bien un café", maisonVoisinInterieur, john, 1, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Je prendrai un thé !", maisonVoisinInterieur, john, 3, game_state)
                pygame.time.wait(n)
                afficher_texte(surface, "L'homme vous laisse un moment seul"+ pron.e()+ " ...", game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Désolé pour l'attente !", maisonVoisinInterieur, john, 2, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Et hop, un café et un thé.", maisonVoisinInterieur, john, 5, game_state)
                pygame.time.wait(n)
 
            if choix == 3:
                afficher_texte_dialogue_utilisateur(surface, "Oh... Non merci !", maisonVoisinInterieur, john, 1, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Pas de soucis !", maisonVoisinInterieur, john, 0, game_state)
            
            afficher_texte_dialogue(surface, "Alors, qu'est-ce qui vous amène ici ?!", maisonVoisinInterieur, john, 3, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Merci beaucoup !", maisonVoisinInterieur, john, 1, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Je viens d'arriver au village alors je me disais que je pourrais vous saluer", maisonVoisinInterieur, john, 6, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "et peut-être vous demander quelques conseils.", maisonVoisinInterieur, john, 6, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Eh bien, en tant que voisins, je suppose que c'est mon devoir !", maisonVoisinInterieur, john, 5, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Je ne vous ai pas demandé votre nom d'ailleurs !", maisonVoisinInterieur, john, 8, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Je m'appelle " + utilisateur.nom +" et vous ?", maisonVoisinInterieur, john, 1, game_state)
            pygame.time.wait(n)
            john.NewNom("John")
            afficher_texte_dialogue(surface, "Je suis John, tu peux me tutoyer !", maisonVoisinInterieur, john, 0, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Enchanté John, tu peux aussi me tutoyer !", maisonVoisinInterieur, john, 6, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Très bien ! Alors de quoi as-tu donc besoin ?", maisonVoisinInterieur, john, 3, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Je ne connais pas bien la ville, est-ce qu'il y a des...", maisonVoisinInterieur, john, 1, game_state)
            pygame.time.wait(n)
            choix = faire_un_choix(maisonVoisinInterieur, "Bars", "Magasins", "Bibliothèques", 3, [1,2,3], game_state)
            if choix  == 1:
                lieu = "bar"
                lp= "d'un"
            elif choix == 2:
                lieu = "magasin"
                lp= "d'un"
            elif choix == 3:
                lieu = "bibliothèque"
                lp="d'une"
            afficher_texte_dialogue_utilisateur(surface, "... des "+ lieu +" ?", maisonVoisinInterieur, john, 6, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Bien sûr !", maisonVoisinInterieur, john, 5, game_state)
            pygame.time.wait(n)
            afficher_texte(surface, "John prend son téléphone,", game_state)
            pygame.time.wait(n)
            afficher_texte(surface, "et vous montre sur une carte la localisation "+ lp + " " +lieu+".", game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Merci beaucoup John, tu me sauves !", maisonVoisinInterieur, john, 6, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Tout le plaisir est pour moi " + utilisateur.nom+".", maisonVoisinInterieur, john, 0, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Bon et bien sur ce, je m'en vais !", maisonVoisinInterieur, john, 1, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Au plaisir de te revoir, n'hésite pas à m'appeler si tu as besoin de quoi que ce soit ! ", maisonVoisinInterieur, john, 4, game_state)
            pygame.time.wait(n)
            afficher_texte(surface, "John vous laisse son numéro de téléphone puis vous raccompagne chez vous.", game_state)
            pygame.time.wait(n)
            return lieu
           
            
    return 0






it1= Boutons(conv(1434,496), "Image/Assert/btn/miniJeux/interrupteur1-1.png", "centre")
it1.resize(conv2(it1.image.get_width(),it1.image.get_height()))
it2= Boutons(conv(1178,1243), "Image/Assert/btn/miniJeux/interrupteur2-1.png", "centre")
it2.resize(conv2(it2.image.get_width(),it2.image.get_height()))
it3= Boutons(conv(580,1252), "Image/Assert/btn/miniJeux/interrupteur3-1.png", "centre")
it3.resize(conv2(it3.image.get_width(),it3.image.get_height()))
it4= Boutons(conv(489,300), "Image/Assert/btn/miniJeux/interrupteur4-1.png", "centre")
it4.resize(conv2(it4.image.get_width(),it4.image.get_height()))




lumiere1=Boutons(conv(1000,720),"Image/Assert/btn/miniJeux/HaloLumiere1.png", "centre")
lumiere1.resize(conv2(lumiere1.image.get_width(),lumiere1.image.get_height()))
lumiere2=Boutons(conv(1000,720),"Image/Assert/btn/miniJeux/HaloLumiere2.png", "centre")
lumiere2.resize(conv2(lumiere2.image.get_width(),lumiere2.image.get_height()))
lumiere3=Boutons(conv(1000,720),"Image/Assert/btn/miniJeux/HaloLumiere3.png", "centre")
lumiere3.resize(conv2(lumiere3.image.get_width(),lumiere3.image.get_height()))
lumiere4=Boutons(conv(1000,720),"Image/Assert/btn/miniJeux/HaloLumiere4.png", "centre")
lumiere4.resize(conv2(lumiere4.image.get_width(),lumiere4.image.get_height()))




def mini_jeu1(game_state):
    gagner=False
    a=0
    b=0
    c=0
    d=0
    while gagner == False:
        surface.fill(0)
        fermer_le_jeu(game_state)
        it1.AffichageBouton(surface)
        it2.AffichageBouton(surface)
        it3.AffichageBouton(surface)
        it4.AffichageBouton(surface)
        lumiere1.AffichageBouton(surface)
        lumiere2.AffichageBouton(surface)
        lumiere3.AffichageBouton(surface)
        lumiere4.AffichageBouton(surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sauvegarde(game_state)
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if it1.positionCentre().collidepoint(event.pos):
                        if "interrupteur1-1" in it1.image1:
                            it1.changeImage("Image/Assert/btn/miniJeux/interrupteur1-2.png")
                            lumiere1.changeImage("Image/Assert/btn/miniJeux/OmbreLumiere1.png")
                            a=1

                    if it2.positionCentre().collidepoint(event.pos):
                        if "interrupteur2-1" in it2.image1:
                            it2.changeImage("Image/Assert/btn/miniJeux/interrupteur2-2.png")
                            lumiere3.changeImage("Image/Assert/btn/miniJeux/OmbreLumiere3.png")
                            b=1

                    if it3.positionCentre().collidepoint(event.pos):
                        if "interrupteur3-1" in it3.image1:
                            it3.changeImage("Image/Assert/btn/miniJeux/interrupteur3-2.png")
                            lumiere2.changeImage("Image/Assert/btn/miniJeux/OmbreLumiere2.png")
                            c=1

                    if it4.positionCentre().collidepoint(event.pos):
                        if "interrupteur4-1" in it4.image1:
                            it4.changeImage("Image/Assert/btn/miniJeux/interrupteur4-2.png")
                            lumiere4.changeImage("Image/Assert/btn/miniJeux/OmbreLumiere4.png")
                            d=1

        if a+b+c+d==4:
            gagner=True

        pygame.display.flip()
                    
                    



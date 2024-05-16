from Programme.choix import *
from Programme.fonctionText import *
from Programme.classPronom import *

n=50
def AlScene1(game_state):
    afficher_texte(surface, "Vous arrivez au parc...", game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "ATTENTION !!", Parc2, utilisateur, 0, game_state)
    pygame.time.wait(n)
    afficher_texte(surface, "Un homme vous bouscule et semble pressé...", game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "(Qu'est-ce qui se passe ici...)", Parc1, utilisateur, 0, game_state)
    pygame.time.wait(n)
    afficher_texte(surface, "Un autre semble chercher quelque chose...", game_state)
    pygame.time.wait(n)
    afficher_texte(surface, "Vous vous approchez de lui...", game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "Bonjour monsieur, y a-t-il un problème ?", Parc1, utilisateur, 3, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue(surface, "Oui, j'ai perdu mon sac...", Parc1, al, 6, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue(surface, "Il y avait un objet très important dedans.", Parc1, al, 11, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue(surface, "Avez-vous vu quelque chose de suspect ?", Parc1, al, 10, game_state)
    pygame.time.wait(n)
    choix = faire_un_choix(Parc1, "Oui", "Non", "", 2, [2,1], game_state)
    if choix== 1:
        afficher_texte_dialogue_utilisateur(surface, "Désolé, je n'ai rien vu de suspect...", Parc1, al, 0, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Ah, dommage", Parc1, al, 6, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Merci quand même...", Parc1, al, 7, game_state)
        pygame.time.wait(n)
        return 0.5
        
    
    if choix== 2:
        afficher_texte_dialogue_utilisateur(surface, "Oui, j'ai vu quelqu'un courir de manière suspecte tout à l'heure.", Parc1, al, 0, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Vraiment ?!", Parc1, al, 12, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Pouvez-vous me dire où vous l'avez vu ?", Parc1, al, 13, game_state)
        pygame.time.wait(n)
        choix = faire_un_choix(Parc1, "Oui", "Non", "", 2, [1,2], game_state)

        if choix== 1 :
            afficher_texte_dialogue_utilisateur(surface, "Oui, je peux vous y conduire.", Parc1, al, 14, game_state)
            pygame.time.wait(n)
            afficher_texte(surface, "Vous emmenez l'homme là où vous avez vu le suspect avec le sac.", game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "C'est mon sac !!", Parc1, al, 12, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Oh non il est vide...", Parc1, al, 5, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "C'était si important pour moi.", Parc1, al, 11, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Si je retrouve la personne qui me l'a volé ! Je lui ferais la peau", Parc1, al, 10, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Merci énormément pour votre aide malgré tout...", Parc1, al, 6, game_state)
            pygame.time.wait(n)
            return 1

        if choix==2:
            afficher_texte_dialogue_utilisateur(surface, "Non, désolé. Je suis pressé.", Parc1, al, 14, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Ah.. D'accord, merci quand même.", Parc1, al, 6, game_state)
            pygame.time.wait(n)
            return 0.5





def AlScene2(pron, game_state):
    afficher_texte_dialogue(surface, "Desolée... C'est une édition limitée, nous ne possédons plus cet article.", Librairie, LaBoulangere, 6, game_state)
    pygame.time.wait(n)
    insister = faire_un_choix(Librairie, "Partir énervé"+ pron.e(), "Insister", "", 2, [0,1], game_state)
    if insister== 1:
        afficher_texte_dialogue(surface, "Je vais vérifier en arrière-boutique... Je ne vous promets rien...", Librairie, LaBoulangere, 6, game_state)
        pygame.time.wait(n)
    afficher_texte(surface, "Vous vous retournez visiblement en colère.", game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "...", Librairie2, utilisateur, 0, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "*BAM*", Librairie3, al, 0, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue(surface, "Oh... Bonjour ! Je me rappelle de vous ! C'est vous qui m'avez aidé à retrouver mon sac la dernière fois !", Librairie, al, 2, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "Oui c'est moi ! Je suis encore désolé de ne pas avoir pu retrouver votre objet...", Librairie, al, 3, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue(surface, "J'ai déposé une plainte à la police, mais je commence à perdre un peu espoir.", Librairie, al, 6, game_state)
    pygame.time.wait(n)
    choix=faire_un_choix(Librairie, "Courage !", "Demander son nom", "", 2, [1,2], game_state)
    if choix == 1:
        afficher_texte_dialogue_utilisateur(surface, "Courage ! Je suis de tout cœur avec vous !", Librairie, al, 1, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Merci beaucoup ! Vous êtes très gentil.", Librairie, al, 7, game_state)
        pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "J'y pense, je ne connais pas votre nom !", Librairie, al, 14, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "Perso je suis "+ utilisateur.nom +" !", Librairie, al, 3, game_state)
    pygame.time.wait(n)
    al.NewNom("Al")
    afficher_texte_dialogue(surface, "Je m'appelle Alphonse Berthier. Mais tout le monde m'appelle Al !", Librairie, al, 2, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue(surface, "D'ailleur tutoyons-nous, non ?", Librairie, al, 7, game_state)
    pygame.time.wait(n)
    afficher_texte_dialogue_utilisateur(surface, "Bien sûr ! Enchanté"+ pron.e()+" Al !", Librairie, al, 3, game_state)
    pygame.time.wait(n)
    choix=faire_un_choix(Librairie, "Au revoir !", "Al Berthier ?", "", 2, [4,3], game_state)
    if choix==3:
        afficher_texte_dialogue_utilisateur(surface, "Attendez ! Vous aviez bien dit Al Berthier ?", Librairie, al, 3, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Alphonse Berthier, c'est ça, pourquoi ?", Librairie, al, 2, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue_utilisateur(surface, "(Je crois avoir déjà vu ce nom quelque part. Où est-ce que c’était… ?)", Librairie, al, 14, game_state)
        pygame.time.wait(n)
        choix=faire_un_choix(Librairie, "Je ne sais plus", "Sur un objet ?", "", 2, [5,6], game_state)
        if choix== 5:
            afficher_texte_dialogue_utilisateur(surface, "Non rien, je n'étais pas sûr d'avoir entendu.", Librairie, al, 3, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "D'accord, sur ce je vais devoir y aller.", Librairie, al, 2, game_state)
            pygame.time.wait(n)
            choix =4
        
        if choix==6:
            afficher_texte_dialogue_utilisateur(surface, "J'ai trouvé un objet avec ton nom dessus.", Librairie, al, 3, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Une montre à gousset ? Avec écrit Al Berthier ?", Librairie, al, 16, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Oui, c'est ça !", Librairie, al, 3, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Est-ce que je peux la voir ?", Librairie, al, 12, game_state)
            pygame.time.wait(n)
            afficher_texte(surface, "Vous sortez l'objet de votre poche", game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "C'est elle !", Librairie, al, 12, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Tenez, elle vous appartient.", Librairie, al, 3, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue(surface, "Merci beaucoup de l'avoir retrouvée !", Librairie, al, 5, game_state)
            pygame.time.wait(n)
            afficher_texte_dialogue_utilisateur(surface, "Tout le plaisir est pour moi Al !", Librairie, al, 3, game_state)
            pygame.time.wait(n)
            if insister==0:
                afficher_texte(surface, "Après vous avoir à nouveau remercié"+pron.e()+"...", game_state)
                pygame.time.wait(n)
                afficher_texte(surface, "Vous échangez vos numéros de téléphone.", game_state)
                pygame.time.wait(n)
            if insister==1:
                afficher_texte_dialogue(surface, "Désolée, j'ai vérifié en arrière-boutique, le dernier a été pris il y a une vingtaine de minutes.", Librairie, LaBoulangere, 6, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Que voulais-tu ?", Librairie, al, 2, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue_utilisateur(surface, "L'édition limitée de la figurine de Wei WuXian...", Librairie, al, 3, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Sérieusement ! Tu parles de ça ?", Librairie, al, 2, game_state)
                pygame.time.wait(n)
                afficher_texte(surface, "Figurine", game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue_utilisateur(surface, "Oui, c'est ça ! Où l'as-tu eu ?!", Librairie, al, 3, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Je l'ai acheté, je fais beaucoup d'achat revente.", Librairie, al, 2, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue_utilisateur(surface, "Oh... Ok.", Librairie, al, 14, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue(surface, "Celui-ci est pour toi !", Librairie, al, 6, game_state)
                pygame.time.wait(n)
                afficher_texte_dialogue_utilisateur(surface, "Quoi ?!", Librairie, al, 3, game_state)
                pygame.time.wait(n)
                afficher_texte(surface, "Vous obtenez un nouvelle objet !", game_state)
                pygame.time.wait(n)
            afficher_texte(surface, "Al vous donne son numero de telephone, et vous salut.", game_state)
            pygame.time.wait(n)

    if choix==4:
        afficher_texte_dialogue_utilisateur(surface, "A bientôt !", Librairie, al, 3, game_state)
        pygame.time.wait(n)
        afficher_texte_dialogue(surface, "Au revoir, à bientôt !", Librairie, al, 2, game_state)
        pygame.time.wait(n)
        
        

            

    
    
    

   
    
    







    

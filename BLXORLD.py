import pygame, sys
from pygame.locals import *
pygame.init()
from lesimport import *
listeTrain=[0,0,0]
try : game_state= ouvrir_sauvegarde()
except: game_state=[0,scene_perso_avancement,0,0,listeTrain, TF]
print(game_state)


start=pygame.image.load('Image/Assert/Accuille/EcranAccuille.png')
start2=pygame.image.load('Image/Assert/Pronom/Fond.png')
start3=pygame.image.load('Image/Assert/NSIcarte/carte.png')
# al= Perso(14, 'AL.png', 600, 600)

jouer= Boutons((widthEcran()/2, heightEcran()/1.7), "Image/Assert/btn/Jouer1.png", "centre")
jouer.resize((jouer.image.get_width()*0.6, jouer.image.get_height()*0.6))

para= Boutons((widthEcran()/2, heightEcran()/1.24), "Image/Assert/btn/Parametre1.png", "centre")
para.resize((para.image.get_width()*0.6, para.image.get_height()*0.6))

ilbtn= Boutons((widthEcran()/3.9, heightEcran()/1.46), "Image/Assert/pronom/Il1.png", "centre" )
ilbtn.resize((ilbtn.image.get_width()*0.7, ilbtn.image.get_height()*0.7))
ellebtn= Boutons((widthEcran()/1.345, heightEcran()/1.46), "Image/Assert/pronom/Elle1.png", "centre" )
ellebtn.resize((ellebtn.image.get_width()*0.7, ellebtn.image.get_height()*0.7))
ielbtn= Boutons((widthEcran()/2, heightEcran()/1.46), "Image/Assert/pronom/Iel1.png", "centre" )
ielbtn.resize((ielbtn.image.get_width()*0.7, ielbtn.image.get_height()*0.7))


destination=""
jeu=1
pron= pronom(game_state[0])
scene_perso_avancement= game_state[1]
utilisateur.nom=game_state[2]
listeTrain= game_state[4]
TF=game_state[5]

def debloquerMaisonAll(TF):
    TF = debloquerMaison(1, TF)
    TF = debloquerMaison(2, TF)
    TF = debloquerMaison(3, TF)
    TF = debloquerMaison(4, TF)
    TF = debloquerMaison(5, TF)
    TF = debloquerMaison(6, TF)
    TF = debloquerMaison(7, TF)
    TF = debloquerMaison(8, TF)
    TF = debloquerMaison(9, TF)
    TF = debloquerMaison(10, TF)
    TF = debloquerMaison(11, TF)
    TF = debloquerMaison(12, TF)
    TF = debloquerMaison(13, TF)
    TF = debloquerMaison(14, TF)
    TF = debloquerMaison(15, TF)


while True :
    #=============================== MENU JOUER ================================
    while jeu==1: 
        PremierAffichage(start)
        CroixAffichage()
        musique.jouer()
        jouer.doubleAffichageBouton("Image/Assert/btn/Jouer1.png","Image/Assert/btn/Jouer2.png", surface)
        para.doubleAffichageBouton("Image/Assert/btn/Parametre1.png","Image/Assert/btn/Parametre2.png", surface)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if croix.positionTopLeft().collidepoint(event.pos):
                        sauvegarde(game_state)
                        pygame.quit()
                        quit()
                    elif jouer.positionCentre().collidepoint(event.pos):
                        if game_state[3]==0:
                            jeu=1.5
                        else: jeu =4

        pygame.display.flip()
    #================================ MENU NOM =================================
    while jeu == 1.5:
        nom(game_state)
        game_state[2]=utilisateur.nom
        if game_state[3]==0:
            jeu=2
        else: jeu =1
    #=============================== MENU PRONOM ===============================
    while jeu==2:
        pygame.display.flip()
        surface.fill(0)
        PremierAffichage(start2)
        CroixAffichage()
        ilbtn.doubleAffichageBouton("Image/Assert/pronom/Il1.png","Image/Assert/pronom/Il2.png", surface)
        ellebtn.doubleAffichageBouton("Image/Assert/pronom/Elle1.png","Image/Assert/pronom/Elle2.png", surface)
        ielbtn.doubleAffichageBouton("Image/Assert/pronom/Iel1.png","Image/Assert/pronom/Iel2.png", surface)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if croix.positionTopLeft().collidepoint(event.pos):
                        sauvegarde(game_state)
                        pygame.quit()
                        quit()
                    elif ilbtn.positionCentre().collidepoint(event.pos):
                        pron=il
                        game_state[0]="il"
                        if game_state[3]==0:
                            jeu=3
                        else : jeu=1

                    elif ielbtn.positionCentre().collidepoint(event.pos):
                        pron=iel
                        game_state[0]="iel"
                        if game_state[3]==0:
                            jeu=3
                        else : jeu=1
                    elif ellebtn.positionCentre().collidepoint(event.pos):
                        pron=elle
                        game_state[0]="elle"
                        if game_state[3]==0:
                            jeu=3
                        else : jeu=1
    #=============================== INTRO AU JEU ==============================
    while jeu==3:
        pygame.display.flip()
        surface.fill(0)
        afficher_texte(surface, "Me voilà enfin seul"+ pron.e()+"...",game_state)
        pygame.time.wait(n)
        surface.fill(0)
        afficher_texte(surface, "Il était temps que je déménage loin de chez mes parents !",game_state)
        pygame.time.wait(n)
        surface.fill(0)
        afficher_texte(surface, "Je vais enfin pouvoir acheter ce que je veux !",game_state)
        pygame.time.wait(n)
        surface.fill(0)
        afficher_texte(surface, "Oh, mais j'y pense, maintenant que je vis seul"+ pron.e()+"...",game_state)
        pygame.time.wait(n)
        surface.fill(0)
        afficher_texte(surface, "Je vais enfin pouvoir collectionner des goodies de BL !",game_state)
        pygame.time.wait(n)
        surface.fill(0)
        afficher_texte(surface, "J'ai hâte de voir ce qu'ils ont dans cette ville...",game_state)
        pygame.time.wait(n)
        surface.fill(0)
        game_state[3]=1
        jeu=4
    #=================================  CARTE  =================================
    if jeu==4:
        maison = fenetre(start3,game_state, TF)
        maison = choix_maison(maison.image1)
    #================================ JOHN SCENE ===============================
    while maison == 1 and scene_perso_avancement[2]==0:         #Debloque un lieu choisi {BAR, MAGASIN, BIBLIOTHEQUE}
        lieu_deblo=JohnScene1(pron,game_state)
        game_state[1][2]=1
        TF = debloquerMaison(15, TF)
        if lieu_deblo=="bar":
            TF = debloquerMaison(6, TF)
        if lieu_deblo=="magasin":
            TF = debloquerMaison(7, TF)
        if lieu_deblo=="bibliothèque":
            TF = debloquerMaison(13, TF)
        bloquerMaison(1, TF)           
        maison=0
        jeu=4
    while maison == 1 and scene_perso_avancement[2]==2:         #Debloque la possibilité que Al viennent et offre un goodies ( condition = avoir le goodies Kusakabe Hikaru)
        mini_jeu1(game_state)
        scene_perso_avancement[2]=2
        jeu=4
        maison=0
    #================================= Al SCENE ================================
    while maison==16 and scene_perso_avancement[0]==0:        #Debloque une futur hisoire avec Al
        scene_perso_avancement[0]= AlScene1(game_state)
        jeu=4
        maison=0
    while maison== 8 and scene_perso_avancement[0]==3:        #LIEU = LIBRAIRIE : Al offre une figurine si on est gentil ! (condition = avoir trouver(volé) la montre au magasin)
        AlScene2(pron, game_state)
        scene_perso_avancement[0]=2
        jeu=4
        maison=0
    #============================ LA BOULANGERE SCENE ==========================
    while maison == 10 and scene_perso_avancement[3]==0:         #Scene bonus, aucune utilité
        LaBoulangereScene1(game_state)
        scene_perso_avancement[3]=1
        game_state[5]=TF
        jeu=4
        maison=0
    #================================ LE TRAIN  ================================
    while maison == 15 and scene_perso_avancement[4]==0:        #premiere scene du parc, de la mosquée, + troisieme lieu a trouver 
        destination, listeTrain=train1(game_state, listeTrain,"Parc","Mosquée","Cimetière", "le", "la", "le")
        if destination=="Parc":
            maison=16
            jeu=0
        if destination=="Mosquée":
            maison=18
            jeu=0
        if destination=="Cimetière":
            maison=20
            jeu=0
        game_state[4]=listeTrain
        if listeTrain==[1,1,1]:
            scene_perso_avancement[4]=1
            listeTrain=[0,0,0]
    
    while maison == 15 and scene_perso_avancement[4]==1:
        destination, listeTrain=train1(game_state, listeTrain,"Cynagogue","Hopitâl","Parc", "la", "l'", "le")
        if destination=="Cynagogue":
            maison=17
            jeu=0
        if destination=="Hopitâl":
            maison=21
            jeu=0
        if destination=="Parc":
            maison=16
            jeu=0
        game_state[4]=listeTrain
        if listeTrain==[1,1,1]:
            scene_perso_avancement[4]=2
    
    while maison == 15 and scene_perso_avancement[4]==1:
        afficher_texte(surface, "Vous arrivez à la gare.", game_state)
        pygame.time.wait(n)
        afficher_texte(surface, "Direction le parc!", game_state)
        maison=16
        jeu=0


#================================ BAR SCENE ================================
    while maison == 6:
        testBar(game_state)
        TF =bloquerMaison(6, TF)
        TF = debloquerMaison(4, TF)
        maison=0
#================================ CINE SCENE ===============================
    while maison == 4:
        testCinema(game_state)
        TF =bloquerMaison(4, TF)
        scene_perso_avancement[2]+=1
        maison=0
#=============================== VOL MAGASIN ===============================
    while maison == 7:
        if scene_perso_avancement[0]==1:
            Montre=True
        Objet = testMagasin(Montre, game_state)
        if Objet=="Lego":
            scene_perso_avancement[0]=1      #changer par le num du perso du dealer

        elif Objet=="Montre":
            Montre=False
            scene_perso_avancement[0]+=1

        maison=0
#============================== MAIRIE SCENE ===============================
    while maison == 9:
        testMairie(game_state)
        TF =bloquerMaison(9, TF)
        maison=0
#============================ BIBLIOTHEQUE SCENE ===========================
    while maison == 13:
        if scene_perso_avancement[0]==2:
            Brochure=True
        Livre=testBibliotheque(Brochure,game_state)

        if Livre=="Brochure":
            scene_perso_avancement[0]+=1
            TF =debloquerMaison(8, TF)

        maison=0



        
"""
goodies :
Porte clef :
0: Sajou Rihito
1: Lan Zhan couché
2: Hikaru Kusakabe
3: Nam Dong Gyun (Dans BJ Alex)
4: Xie Lian
5: Xie Lian x Hua Cheng
6: Hua Cheng
7: Sato Mafuyu
8: Painter of the night
9: Lapin mdzs
10: top pearl boy
11: btm pearl boy
12: Uenoyama
13: Chibi Mo Dao Zu Shi
14: Soumi BJ Alex
15: Maitre BJ Alex
16: BJ Alex
"""
"""
1: Maison voisin
2: 
3: 
4: Cinema
5: Ecole
6: Bar
7: Magasin
8: Librairie
9: Mairie
10: Boulangerie
11: Café
12: Eglise
13: Bibliotheque
14: Maison au dessus du train
15: Train

16: Parc
17: Cynagogue
18: Mosquée
20: Cimetiere
21: Hopital
"""
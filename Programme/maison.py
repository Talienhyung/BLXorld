import pygame
from Programme.fonctionAffichage import *
from Programme.classImage import *
from Programme.conv import *
from Programme.fermer import *



m1=Image("Image/Assert/NSIcarte/f1/m1.png")
m1.resize(conv2(m1.original_image.get_width(),m1.original_image.get_height()))
f1_1= Boutons(conv(1272,969),"Image/Assert/NSIcarte/f1/f1-1.png","centre")
f1_1.resize(conv2(f1_1.image.get_width(),f1_1.image.get_height()))
f1_2= Boutons(conv(1174,1113),"Image/Assert/NSIcarte/f1/f1-2.png","centre")
f1_2.resize(conv2(f1_2.image.get_width(),f1_2.image.get_height()))
f1_3= Boutons(conv(1274,1115),"Image/Assert/NSIcarte/f1/f1-3.png","centre")
f1_3.resize(conv2(f1_3.image.get_width(),f1_3.image.get_height()))
f1_4= Boutons(conv(1034,1125),"Image/Assert/NSIcarte/f1/f1-4.png","centre")
f1_4.resize(conv2(f1_4.image.get_width(),f1_4.image.get_height()))
f1_5= Boutons(conv(938,1137),"Image/Assert/NSIcarte/f1/f1-5.png","centre")
f1_5.resize(conv2(f1_5.image.get_width(),f1_5.image.get_height()))
l1=[f1_1, f1_2, f1_3, f1_4,f1_5]

m2=Image("Image/Assert/NSIcarte/f2/m2.png")
m2.resize(conv2(m2.original_image.get_width(),m2.original_image.get_height()))
f2_1= Boutons(conv(1498,1028),"Image/Assert/NSIcarte/f2/f2-1.png","centre")
f2_1.resize(conv2(f2_1.image.get_width(),f2_1.image.get_height()))
f2_2= Boutons(conv(1501,1178),"Image/Assert/NSIcarte/f2/f2-2.png","centre")
f2_2.resize(conv2(f2_2.image.get_width(),f2_2.image.get_height()))
f2_3= Boutons(conv(1377,1177),"Image/Assert/NSIcarte/f2/f2-3.png","centre")
f2_3.resize(conv2(f2_3.image.get_width(),f2_3.image.get_height()))
l2=[f2_1, f2_2, f2_3]

m3=Image("Image/Assert/NSIcarte/f3/m3.png")
m3.resize(conv2(m3.original_image.get_width(),m3.original_image.get_height()))
f3_1= Boutons(conv(646,1342),"Image/Assert/NSIcarte/f3/f3-1.png","centre")
f3_1.resize(conv2(f3_1.image.get_width(),f3_1.image.get_height()))
f3_2= Boutons(conv(784,1234),"Image/Assert/NSIcarte/f3/f3-2.png","centre")
f3_2.resize(conv2(f3_2.image.get_width(),f3_2.image.get_height()))
f3_3= Boutons(conv(886,1235),"Image/Assert/NSIcarte/f3/f3-3.png","centre")
f3_3.resize(conv2(f3_3.image.get_width(),f3_3.image.get_height()))
f3_4= Boutons(conv(799,1360),"Image/Assert/NSIcarte/f3/f3-4.png","centre")
f3_4.resize(conv2(f3_4.image.get_width(),f3_4.image.get_height()))
f3_5= Boutons(conv(884,1357),"Image/Assert/NSIcarte/f3/f3-5.png","centre")
f3_5.resize(conv2(f3_5.image.get_width(),f3_5.image.get_height()))
f3_6= Boutons(conv(652,1216),"Image/Assert/NSIcarte/f3/f3-6.png","centre")
f3_6.resize(conv2(f3_6.image.get_width(),f3_6.image.get_height()))
l3=[f3_1,f3_2,f3_3,f3_4,f3_5,f3_6]

m4=Image("Image/Assert/NSIcarte/f4/m4.png")
m4.resize(conv2(m4.original_image.get_width(),m4.original_image.get_height()))
f4_1= Boutons(conv(661,1028),"Image/Assert/NSIcarte/f4/f4-1.png","centre")
f4_1.resize(conv2(f4_1.image.get_width(),f4_1.image.get_height()))
f4_2= Boutons(conv(795,1025),"Image/Assert/NSIcarte/f4/f4-2.png","centre")
f4_2.resize(conv2(f4_2.image.get_width(),f4_2.image.get_height()))
l4=[f4_1,f4_2]

m5=Image("Image/Assert/NSIcarte/f5/m5.png")
m5.resize(conv2(m5.original_image.get_width(),m5.original_image.get_height()))
f5_1= Boutons(conv(463,1061),"Image/Assert/NSIcarte/f5/f5-1.png","centre")
f5_1.resize(conv2(f5_1.image.get_width(),f5_1.image.get_height()))
f5_2= Boutons(conv(531,981),"Image/Assert/NSIcarte/f5/f5-2.png","centre")
f5_2.resize(conv2(f5_2.image.get_width(),f5_2.image.get_height()))
f5_3= Boutons(conv(548,1163),"Image/Assert/NSIcarte/f5/f5-3.png","centre")
f5_3.resize(conv2(f5_3.image.get_width(),f5_3.image.get_height()))
l5=[f5_1,f5_2,f5_3]

m6=Image("Image/Assert/NSIcarte/f6/m6.png")
m6.resize(conv2(m6.original_image.get_width(),m6.original_image.get_height()))
f6_1= Boutons(conv(1958,1271),"Image/Assert/NSIcarte/f6/f6-1.png","centre")
f6_1.resize(conv2(f6_1.image.get_width(),f6_1.image.get_height()))
f6_2= Boutons(conv(1872,1275),"Image/Assert/NSIcarte/f6/f6-2.png","centre")
f6_2.resize(conv2(f6_2.image.get_width(),f6_2.image.get_height()))
f6_3= Boutons(conv(1790,1275),"Image/Assert/NSIcarte/f6/f6-3.png","centre")
f6_3.resize(conv2(f6_3.image.get_width(),f6_3.image.get_height()))
l6=[f6_1,f6_2,f6_3]

m7=Image("Image/Assert/NSIcarte/f7/m7.png")
m7.resize(conv2(m7.original_image.get_width(),m7.original_image.get_height()))
f7_1= Boutons(conv(1638,1037),"Image/Assert/NSIcarte/f7/f7-1.png","centre")
f7_1.resize(conv2(f7_1.image.get_width(),f7_1.image.get_height()))
f7_2= Boutons(conv(1915,908),"Image/Assert/NSIcarte/f7/f7-2.png","centre")
f7_2.resize(conv2(f7_2.image.get_width(),f7_2.image.get_height()))
f7_3= Boutons(conv(1850,1017),"Image/Assert/NSIcarte/f7/f7-3.png","centre")
f7_3.resize(conv2(f7_3.image.get_width(),f7_3.image.get_height()))
f7_4= Boutons(conv(1728,1049),"Image/Assert/NSIcarte/f7/f7-4.png","centre")
f7_4.resize(conv2(f7_4.image.get_width(),f7_4.image.get_height()))
l7=[f7_1,f7_2,f7_3,f7_4]

m8=Image("Image/Assert/NSIcarte/f8/m8.png")
m8.resize(conv2(m8.original_image.get_width(),m8.original_image.get_height()))
f8_1= Boutons(conv(1024,823),"Image/Assert/NSIcarte/f8/f8-1.png","centre")
f8_1.resize(conv2(f8_1.image.get_width(),f8_1.image.get_height()))
f8_2= Boutons(conv(972,837),"Image/Assert/NSIcarte/f8/f8-2.png","centre")
f8_2.resize(conv2(f8_2.image.get_width(),f8_2.image.get_height()))
f8_3= Boutons(conv(1079,840),"Image/Assert/NSIcarte/f8/f8-3.png","centre")
f8_3.resize(conv2(f8_3.image.get_width(),f8_3.image.get_height()))
f8_4= Boutons(conv(892,904),"Image/Assert/NSIcarte/f8/f8-4.png","centre")
f8_4.resize(conv2(f8_4.image.get_width(),f8_4.image.get_height()))
l8=[f8_1,f8_2,f8_3,f8_4]

m9=Image("Image/Assert/NSIcarte/f9/m9.png")
m9.resize(conv2(m9.original_image.get_width(),m9.original_image.get_height()))
f9_1= Boutons(conv(1637,759),"Image/Assert/NSIcarte/f9/f9-1.png","centre")
f9_1.resize(conv2(f9_1.image.get_width(),f9_1.image.get_height()))
f9_2= Boutons(conv(1595,759),"Image/Assert/NSIcarte/f9/f9-2.png","centre")
f9_2.resize(conv2(f9_2.image.get_width(),f9_2.image.get_height()))
f9_3= Boutons(conv(1333,712),"Image/Assert/NSIcarte/f9/f9-3.png","centre")
f9_3.resize(conv2(f9_3.image.get_width(),f9_3.image.get_height()))
f9_4= Boutons(conv(1528,684),"Image/Assert/NSIcarte/f9/f9-4.png","centre")
f9_4.resize(conv2(f9_4.image.get_width(),f9_4.image.get_height()))
f9_5= Boutons(conv(1558,619),"Image/Assert/NSIcarte/f9/f9-5.png","centre")
f9_5.resize(conv2(f9_5.image.get_width(),f9_5.image.get_height()))
f9_6= Boutons(conv(1636,824),"Image/Assert/NSIcarte/f9/f9-6.png","centre")
f9_6.resize(conv2(f9_6.image.get_width(),f9_6.image.get_height()))
f9_7= Boutons(conv(1528,856),"Image/Assert/NSIcarte/f9/f9-7.png","centre")
f9_7.resize(conv2(f9_7.image.get_width(),f9_7.image.get_height()))
f9_8= Boutons(conv(1392,731),"Image/Assert/NSIcarte/f9/f9-8.png","centre")
f9_8.resize(conv2(f9_8.image.get_width(),f9_8.image.get_height()))
f9_9= Boutons(conv(1503,750),"Image/Assert/NSIcarte/f9/f9-9.png","centre")
f9_9.resize(conv2(f9_9.image.get_width(),f9_9.image.get_height()))
l9=[f9_1,f9_2,f9_3,f9_4,f9_5,f9_6,f9_7,f9_8,f9_9]

m10=Image("Image/Assert/NSIcarte/f10/m10.png")
m10.resize(conv2(m10.original_image.get_width(),m10.original_image.get_height()))
f10_1= Boutons(conv(645,701),"Image/Assert/NSIcarte/f10/f10-1.png","centre")
f10_1.resize(conv2(f10_1.image.get_width(),f10_1.image.get_height()))
f10_2= Boutons(conv(610,779),"Image/Assert/NSIcarte/f10/f10-2.png","centre")
f10_2.resize(conv2(f10_2.image.get_width(),f10_2.image.get_height()))
f10_3= Boutons(conv(675,779),"Image/Assert/NSIcarte/f10/f10-3.png","centre")
f10_3.resize(conv2(f10_3.image.get_width(),f10_3.image.get_height()))
l10=[f10_1,f10_2,f10_3]

m11=Image("Image/Assert/NSIcarte/f11/m11.png")
m11.resize(conv2(m11.original_image.get_width(),m11.original_image.get_height()))
f11_1= Boutons(conv(1684,454),"Image/Assert/NSIcarte/f11/f11-1.png","centre")
f11_1.resize(conv2(f11_1.image.get_width(),f11_1.image.get_height()))
f11_2= Boutons(conv(1714,457),"Image/Assert/NSIcarte/f11/f11-2.png","centre")
f11_2.resize(conv2(f11_2.image.get_width(),f11_2.image.get_height()))
f11_3= Boutons(conv(1745,469),"Image/Assert/NSIcarte/f11/f11-3.png","centre")
f11_3.resize(conv2(f11_3.image.get_width(),f11_3.image.get_height()))
f11_4= Boutons(conv(1721,510),"Image/Assert/NSIcarte/f11/f11-4.png","centre")
f11_4.resize(conv2(f11_4.image.get_width(),f11_4.image.get_height()))
f11_5= Boutons(conv(1619,519),"Image/Assert/NSIcarte/f11/f11-5.png","centre")
f11_5.resize(conv2(f11_5.image.get_width(),f11_5.image.get_height()))
f11_6= Boutons(conv(1665,561),"Image/Assert/NSIcarte/f11/f11-6.png","centre")
f11_6.resize(conv2(f11_6.image.get_width(),f11_6.image.get_height()))
f11_7= Boutons(conv(1799,589),"Image/Assert/NSIcarte/f11/f11-7.png","centre")
f11_7.resize(conv2(f11_7.image.get_width(),f11_7.image.get_height()))
l11=[f11_1,f11_2,f11_3,f11_4,f11_5,f11_6,f11_7]


m12=Image("Image/Assert/NSIcarte/f12/m12.png")
m12.resize(conv2(m12.original_image.get_width(),m12.original_image.get_height()))
f12_1= Boutons(conv(1241,386),"Image/Assert/NSIcarte/f12/f12-1.png","centre")
f12_1.resize(conv2(f12_1.image.get_width(),f12_1.image.get_height()))
f12_2= Boutons(conv(1214,295),"Image/Assert/NSIcarte/f12/f12-2.png","centre")
f12_2.resize(conv2(f12_2.image.get_width(),f12_2.image.get_height()))
f12_3= Boutons(conv(996,486),"Image/Assert/NSIcarte/f12/f12-3.png","centre")
f12_3.resize(conv2(f12_3.image.get_width(),f12_3.image.get_height()))
f12_4= Boutons(conv(963,621),"Image/Assert/NSIcarte/f12/f12-4.png","centre")
f12_4.resize(conv2(f12_4.image.get_width(),f12_4.image.get_height()))
f12_5= Boutons(conv(966,549),"Image/Assert/NSIcarte/f12/f12-5.png","centre")
f12_5.resize(conv2(f12_5.image.get_width(),f12_5.image.get_height()))
f12_6= Boutons(conv(1251,551),"Image/Assert/NSIcarte/f12/f12-6.png","centre")
f12_6.resize(conv2(f12_6.image.get_width(),f12_6.image.get_height()))
f12_7= Boutons(conv(1327,455),"Image/Assert/NSIcarte/f12/f12-7.png","centre")
f12_7.resize(conv2(f12_7.image.get_width(),f12_7.image.get_height()))
f12_8= Boutons(conv(1166,442),"Image/Assert/NSIcarte/f12/f12-8.png","centre")
f12_8.resize(conv2(f12_8.image.get_width(),f12_8.image.get_height()))
f12_9= Boutons(conv(1146,525),"Image/Assert/NSIcarte/f12/f12-9.png","centre")
f12_9.resize(conv2(f12_9.image.get_width(),f12_9.image.get_height()))
f12_10= Boutons(conv(1350,541),"Image/Assert/NSIcarte/f12/f12-10.png","centre")
f12_10.resize(conv2(f12_10.image.get_width(),f12_10.image.get_height()))
l12=[f12_1,f12_2,f12_3,f12_4,f12_5,f12_6,f12_7,f12_8,f12_9,f12_10]

m13=Image("Image/Assert/NSIcarte/f13/m13.png")
m13.resize(conv2(m13.original_image.get_width(),m13.original_image.get_height()))
f13_1= Boutons(conv(778,121),"Image/Assert/NSIcarte/f13/f13-1.png","centre")
f13_1.resize(conv2(f13_1.image.get_width(),f13_1.image.get_height()))
f13_2= Boutons(conv(778,84),"Image/Assert/NSIcarte/f13/f13-2.png","centre")
f13_2.resize(conv2(f13_2.image.get_width(),f13_2.image.get_height()))
f13_3= Boutons(conv(780,167),"Image/Assert/NSIcarte/f13/f13-3.png","centre")
f13_3.resize(conv2(f13_3.image.get_width(),f13_3.image.get_height()))
f13_4= Boutons(conv(788,296),"Image/Assert/NSIcarte/f13/f13-4.png","centre")
f13_4.resize(conv2(f13_4.image.get_width(),f13_4.image.get_height()))
l13=[f13_1,f13_2,f13_3,f13_4]

m14=Image("Image/Assert/NSIcarte/f14/m14.png")
m14.resize(conv2(m14.original_image.get_width(),m14.original_image.get_height()))
f14_1= Boutons(conv(309,691),"Image/Assert/NSIcarte/f14/f14-1.png","centre")
f14_1.resize(conv2(f14_1.image.get_width(),f14_1.image.get_height()))
l14=[f14_1]

m15=Image("Image/Assert/NSIcarte/f15/m15.png")
m15.resize(conv2(m15.original_image.get_width(),m15.original_image.get_height()))
f15_1= Boutons(conv(290,1233),"Image/Assert/NSIcarte/f15/f15-1.png","centre")
f15_1.resize(conv2(f15_1.image.get_width(),f15_1.image.get_height()))
l15=[f15_1]


ListeM=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15]
ListeL=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15]
TF=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
terre=1

def debloquerMaison(maison, liste):
    liste[maison-1]=1
    TF[maison-1]=1
    return liste
    

def bloquerMaison(maison, liste):
    liste[maison-1]=0
    TF[maison-1]=0
    return liste



def fenetre(start3,game_state, TF, e=1):
    op = 1
    while e==1:
        pygame.display.flip()
        surface.fill(0)
        PremierAffichage(start3)
        fermer_le_jeu(game_state)
        for i in range (len(ListeL)):
            if TF[i]==1:
                for j in ListeL[i]:
                    j.AffichageBouton(surface)
                    if j.colli():
                        ListeM[i].draw(surface,(l,0))
                        e= mapAccess(j)
                        if e !=1 and op==1 : op=j

    return op

def choix_maison(image):
    if "f1/" in image:
        return 1
    elif "f2/" in image:
        return 2
    elif "f3/" in image:
        return 3
    elif "f4/" in image:
        return 4
    elif "f5/" in image:
        return 5
    elif "f6/" in image:
        return 6
    elif "f7/" in image:
        return 7
    elif "f8/" in image:
        return 8
    elif "f9/" in image:
        return 9
    elif "f10/" in image:
        return 10
    elif "f11/" in image:
        return 11
    elif "f12/" in image:
        return 12
    elif "f13/" in image:
        return 13
    elif "f14/" in image:
        return 14
    elif "f15/" in image:
        return 15
    

        
    

                        
                            
import pygame
from Programme.fonctionAffichage import *

im=pygame.image.load("Image/Assert/NSIcarte/carte.png")
l, w=Choper_le_centre(im)
h= heightEcran()

def conv(wi,hi):
    nw=l+(wi/2000)*w
    nh=(hi/1440)*h
    return (nw,nh)

def conv2(wi,hi):
    nw=(wi/2000)*w
    nh=(hi/1440)*h
    return (nw,nh)
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyxel
import random


pyxel.init(256, 256, title="Casse_Brique")

plateforme_x = 103
plateforme_y = 240
balle = False
x = plateforme_x + 25
y = plateforme_y - 3
vitesse = 3
rayon = 2
balle_liste = [x, y]
vitesse_balle_x = 3
vitesse_balle_y = 3


def plateforme_deplacement(plateforme_x, plateforme_y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if plateforme_x < 206 : plateforme_x += vitesse

    if pyxel.btn(pyxel.KEY_LEFT):
        if plateforme_x > 0 : plateforme_x -= vitesse

    return plateforme_x, plateforme_y


def balle_deplacement(x, y):

    global vitesse_balle_x, vitesse_balle_y
    x -= vitesse_balle_x
    y -= vitesse_balle_y
    if y <= 2 :
        vitesse_balle_x = vitesse_balle_x
        vitesse_balle_y = -vitesse_balle_y
    elif x <= 2 :
        vitesse_balle_x = -vitesse_balle_x
        vitesse_balle_y = vitesse_balle_y
    elif x >= 254 :
        vitesse_balle_x = -vitesse_balle_x
        vitesse_balle_y = vitesse_balle_y
    return x, y

def update():

    global plateforme_x, plateforme_y, balle_liste, brique_liste, x, y, balle
    plateforme_x, plateforme_y = plateforme_deplacement(plateforme_x, plateforme_y)
    if pyxel.btn(pyxel.KEY_SPACE):
        balle = True
    if balle == True:
        x, y = balle_deplacement(x, y)


def draw():

    pyxel.cls(0)
    pyxel.circ(x, y, rayon, 2)
    pyxel.rect(plateforme_x, plateforme_y, 50, 6, 1)


pyxel.run(update, draw)

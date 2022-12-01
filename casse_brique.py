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
vitesse_balle_x = 4
vitesse_balle_y = 3
vie = 3
score = 0


def plateforme_deplacement(plateforme_x, plateforme_y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if plateforme_x < 206 : plateforme_x += vitesse

    if pyxel.btn(pyxel.KEY_LEFT):
        if plateforme_x > 0 : plateforme_x -= vitesse

    return plateforme_x, plateforme_y


def balle_deplacement(x, y):

    global vitesse_balle_x, vitesse_balle_y, balle, vie
    x -= vitesse_balle_x
    y -= vitesse_balle_y
    if y <= rayon :
        vitesse_balle_x = vitesse_balle_x
        vitesse_balle_y = -vitesse_balle_y
    elif x <= rayon :
        vitesse_balle_x = -vitesse_balle_x
        vitesse_balle_y = vitesse_balle_y
    elif x >= (256-rayon) :
        vitesse_balle_x = -vitesse_balle_x
        vitesse_balle_y = vitesse_balle_y
    elif y >= (240-rayon):
        if (plateforme_x-rayon)<x<(plateforme_x+50-rayon) :
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
        elif (plateforme_x-rayon)>x:
            vie -= 1
            balle = False
        elif x>(plateforme_x+50-rayon) :
            vie -= 1
            balle = False
    return x, y


def update():

    global plateforme_x, plateforme_y, balle_liste, brique_liste, x, y, balle, vie
    plateforme_x, plateforme_y = plateforme_deplacement(plateforme_x, plateforme_y)
    if balle is False :
        x, y = (plateforme_x+25), (plateforme_y-3)
    if pyxel.btnr(pyxel.KEY_SPACE):
        balle = True
    if balle is True:
        x, y = balle_deplacement(x, y)


def draw():

    pyxel.cls(0)
    pyxel.text(200, 10,"score : %s " % str(score), 7)
    pyxel.text(200, 20,"vie : %s " %str(vie), 7)
    pyxel.circ(x, y, rayon, 2)
    pyxel.rect(plateforme_x, plateforme_y, 50, 6, 1)


pyxel.run(update, draw)
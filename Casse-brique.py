import pyxel
import random


pyxel.init(256, 256, title="Casse_Brique")
pyxel.load("ressources/objects.pyxres")
plateforme_x = 108
plateforme_y = 240
balle = False
x = plateforme_x + 20
y = plateforme_y - 3
vitesse = 3
rayon = 2 
balle_liste = [x, y]
vitesse_balle_x = 5
vitesse_balle_y = 5
vitesse_brique = 2
vitesse__brique = 2
brique2_x = 0
brique2_y = 92
brique2_xx = 226
brique2_yy = 82
vie = 3
score = 0
brique_x = [1, 33, 65, 97, 129, 161, 193, 225, 1, 33, 193, 225, 1, 225, 1, 97, 129, 225, 1, 225, 1, 33, 193, 225]
brique_y = [2, 2, 2, 2, 2, 2, 2, 2, 12, 12, 12, 12, 22, 22, 32, 32, 32, 32, 42, 42, 52, 52, 52, 52]
brique3_x = [1, 225]
brique3_y = [62, 62]
bxx = 0
byy = 0
b3x = 0
b3y = 0
brique1 = True
brique2 = True
brique2_etat = True
brique2__etat = True
jeu = True
balle_vb = True
couleur = random.randint(0, 15)


def plateforme_deplacement(plateforme_x, plateforme_y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if plateforme_x < 206:
            plateforme_x += vitesse
    if pyxel.btn(pyxel.KEY_LEFT):
        if plateforme_x > 0:
            plateforme_x -= vitesse
    return plateforme_x, plateforme_y


def balle_deplacement(x, y):

    global vitesse_balle_x, vitesse_balle_y, balle, vie
    x -= vitesse_balle_x
    y -= vitesse_balle_y
    if y <= rayon:
        vitesse_balle_x = vitesse_balle_x
        vitesse_balle_y = -vitesse_balle_y
    elif x <= rayon:
        vitesse_balle_x = -vitesse_balle_x
        vitesse_balle_y = vitesse_balle_y
    elif x >= (256-rayon):
        vitesse_balle_x = -vitesse_balle_x
        vitesse_balle_y = vitesse_balle_y
    elif y >= (240-rayon):
        if (plateforme_x-rayon) < x < (plateforme_x+50-rayon):
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
        elif (plateforme_x+40+rayon) < x < (plateforme_x+60-rayon):
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
        elif (plateforme_x-rayon) > x > (plateforme_x-20+rayon):
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
        elif (plateforme_x+60-rayon) > x:
            if y >= 243:
                vie -= 1
                balle = False
        elif x > (plateforme_x+50-rayon):
            if y >= 243:
                vie -= 1
                balle = False
    return x, y


def brique_supression():

    global x, y, brique_x, brique_y, vitesse_balle_x, vitesse_balle_y, score, brique1, rayon
    for i in range(0, len(brique_x)):
        if (brique_x[i]+30+rayon) >= x >= (brique_x[i]-rayon) and y == (brique_y[i] + 8 + rayon):
            brique_x.pop(i)
            brique_y.pop(i)
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
            score += 50
            break
        elif (brique_x[i] + 30 + rayon) >= x >= (brique_x[i] - rayon) and (brique_y[i] - rayon) == y:
            brique_x.pop(i)
            brique_y.pop(i)
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
            score += 50
            break
        elif (brique_x[i] + 30 + rayon) >= x >= (brique_x[i] - rayon) and (brique_y[i]) < y < (brique_y[i] + 8):
            brique_x.pop(i)
            brique_y.pop(i)
            vitesse_balle_x = -vitesse_balle_x
            vitesse_balle_y = vitesse_balle_y
            score += 50
            break
    if len(brique_x) == 0:
        brique1 = False
    return brique_x, brique_y, vitesse_balle_x, vitesse_balle_y


def brique3_rebond():

    global x, y, brique3_x, brique3_y, vitesse_balle_x, vitesse_balle_y
    for h in range(0, len(brique3_x)):
        if (brique3_x[h]+30+rayon) >= x >= (brique3_x[h]-rayon) and y == (brique3_y[h] + 8 + rayon):
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
        elif (brique3_x[h]+30+rayon) >= x >= (brique3_x[h]-rayon) and (brique3_y[h]-rayon) == y:
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
        elif (brique3_x[h]+30+rayon) >= x >= (brique3_x[h]-rayon) and (brique3_y[h]) < y < (brique3_y[h] + 8):
            vitesse_balle_x = -vitesse_balle_x
            vitesse_balle_y = vitesse_balle_y
    return vitesse_balle_x, vitesse_balle_y


def brique2_deplacement():

    global vitesse_brique, x, y, brique2_x
    brique2_x += vitesse_brique
    if brique2_x == 0:
        vitesse_brique = -vitesse_brique
    if brique2_x == 226:
        vitesse_brique = -vitesse_brique
    return brique2_x


def brique2_supression():

    global brique2_etat, x, y, vitesse_balle_y, score
    if brique2_etat is True:
        if (brique2_x - rayon) < x < (brique2_x + 30 + rayon) and (brique2_y - rayon) < y < (brique2_y + 8 + rayon):
            brique2_etat = False
            vitesse_balle_y = -vitesse_balle_y
            score += 100
    return brique2_etat, vitesse_balle_y, score


def brique2__deplacement():

    global vitesse__brique, x, y, brique2__etat, brique2_xx
    brique2_xx -= vitesse__brique
    if brique2_xx == 0:
        vitesse__brique = -vitesse__brique
    if brique2_xx == 226:
        vitesse__brique = -vitesse__brique
    return brique2_xx


def brique2__supression():

    global brique2__etat, x, y, vitesse_balle_y, score
    if brique2__etat is True:
        if (brique2_xx-rayon) < x < (brique2_xx+30+rayon) and (brique2_yy-rayon) < y < (brique2_yy+8+rayon):
            brique2__etat = False
            vitesse_balle_y = -vitesse_balle_y
            score += 100
    return brique2__etat, vitesse_balle_y, score


def fin():

    global brique2_etat, brique2__etat, brique2, brique1, jeu
    if brique2_etat is False:
        if brique2__etat is False:
            if brique1 is False:
                jeu = False
    return jeu


def update():

    global plateforme_x, plateforme_y, balle_liste, x, y, balle, vie, bxx, byy, brique_x, brique_y, brique2_x, brique2_xx, jeu, score, vitesse_balle_x, vitesse_balle_y, balle_vb
    plateforme_x, plateforme_y = plateforme_deplacement(plateforme_x, plateforme_y)
    brique2_x = brique2_deplacement()
    brique2_xx = brique2__deplacement()
    fin()
    if balle is False:
        x, y = (plateforme_x+20), (plateforme_y-3)
    if pyxel.btnr(pyxel.KEY_SPACE):
        balle = True
    if balle is True:
        x, y = balle_deplacement(x, y)
        brique_supression()
        brique2_supression()
        brique2__supression()
        brique3_rebond()


def draw():

    pyxel.cls(0)
   
    if jeu is True:
        if vie > 0:
            if balle is False:
                pyxel.text(90, 200, "Espace pour commencer", 7)
            if brique2_etat is True:
                pyxel.blt(brique2_x, brique2_y, 0, 0, 9, 30, 8, )
            if brique2__etat is True:
                pyxel.blt(brique2_xx, brique2_yy, 0, 0, 9, 30, 8, )
            for n in range(0, len(brique_x)):
                bxx = brique_x[n]
                byy = brique_y[n]
                pyxel.blt(bxx, byy, 0, 0, 1, 30, 8, )
            for q in range(0, len(brique3_x)):
                b3x = brique3_x[q]
                b3y = brique3_y[q]
                pyxel.blt(b3x, b3y, 0, 0, 17, 30, 8, )
            pyxel.text(200, 225, "score : %s " % str(score), 7)
            pyxel.text(200, 215, "vie : %s " % str(vie), 7)
            pyxel.circ(x, y, rayon, 2)
            pyxel.rect(plateforme_x, plateforme_y, 40, 8, 1)
            pyxel.tri(plateforme_x, plateforme_y, plateforme_x, (plateforme_y+7), (plateforme_x-20), (plateforme_y+7), 1)
            pyxel.tri((plateforme_x+40), plateforme_y, (plateforme_x+40), (plateforme_y + 7), (plateforme_x+60), (plateforme_y + 7), 1)
        else:
            pyxel.text(100, 118, "GAME OVER !", 7)
            pyxel.text(98, 128, "Tu as perdu.", 7)
    else:
        pyxel.text(108, 118, "BRAVO !", 7)
        pyxel.text(105, 128, "You win.", 7)


pyxel.run(update, draw)

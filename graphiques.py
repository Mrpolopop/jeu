import pyxel


def coeurs(coeur_p1, coeur_p2):

    # joueur 1

    if coeur_p1 == 3:
        pyxel.blt(x=28, y=4, img=0, u=19, v=0, w=10, h=10)

    if coeur_p1 >= 2:
        pyxel.blt(x=16, y=4, img=0, u=19, v=0, w=10, h=10)

    if coeur_p1 >= 1:
        pyxel.blt(x=4, y=4, img=0, u=19, v=0, w=10, h=10)

    # joueur 2

    if coeur_p2 == 3:
        pyxel.blt(x=90, y=4, img=0, u=19, v=0, w=10, h=10)

    if coeur_p2 >= 2:
        pyxel.blt(x=102, y=4, img=0, u=19, v=0, w=10, h=10)

    if coeur_p2 >= 1:
        pyxel.blt(x=114, y=4, img=0, u=19, v=0, w=10, h=10)


def vie(vie_p1, vie_p2):

    # joueur 1
    # barre
    pyxel.blt(x=4, y=16, img=0, u=72, v=0, w=16, h=3)

    # vie
    if vie_p1 == 5:
        pyxel.blt(x=17, y=17, img=0, u=72, v=4, w=2, h=1)

    if vie_p1 >= 4:
        pyxel.blt(x=14, y=17, img=0, u=72, v=4, w=2, h=1)

    if vie_p1 >= 3:
        pyxel.blt(x=11, y=17, img=0, u=72, v=4, w=2, h=1)

    if vie_p1 >= 2:
        pyxel.blt(x=8, y=17, img=0, u=72, v=4, w=2, h=1)

    if vie_p1 >= 1:
        pyxel.blt(x=5, y=17, img=0, u=72, v=4, w=2, h=1)

    # joueur 2
    # barre
    pyxel.blt(x=108, y=16, img=0, u=72, v=0, w=16, h=3)

    # vie
    if vie_p2 == 5:
        pyxel.blt(x=109, y=17, img=0, u=72, v=4, w=2, h=1)

    if vie_p2 >= 4:
        pyxel.blt(x=112, y=17, img=0, u=72, v=4, w=2, h=1)

    if vie_p2 >= 3:
        pyxel.blt(x=115, y=17, img=0, u=72, v=4, w=2, h=1)

    if vie_p2 >= 2:
        pyxel.blt(x=118, y=17, img=0, u=72, v=4, w=2, h=1)

    if vie_p2 >= 1:
        pyxel.blt(x=121, y=17, img=0, u=72, v=4, w=2, h=1)

import pyxel
import player
import graphiques
import time as t

fps = 29
vitesse = 1
vit_kunai = 2.5
vit_ult = 6

p1 = player.Player(1, vitesse=vitesse, vit_kunai=vit_kunai, vit_ult=vit_ult)
p2 = player.Player(2, vitesse=vitesse, vit_kunai=vit_kunai, vit_ult=vit_ult)

pyxel.init(128, 128, title="Morthal Basthon", fps=fps)
pyxel.load("res.pyxres")


def update():
    # personnages
    p1.pos_update()
    p2.pos_update()

    # kunais
    p1.kunai_update()
    p2.kunai_update()

    kunai_p2 = p1.position['x'] < p2.pos_kunai['x'] < p1.position['x'] + 6 and \
               p1.position['y'] - 1 < p2.pos_kunai['y'] + 1 < p1.position['y'] + 8

    kunai_p1 = p2.position['x'] < p1.pos_kunai['x'] + 4 < p2.position['x'] + 6 and \
               p2.position['y'] - 1 < p1.pos_kunai['y'] + 1 < p2.position['y'] + 8

    if kunai_p2:
        p1.vie_update()

    if kunai_p1:
        p2.vie_update()

    if p1.coeur == 0 or p2.coeur == 0:
        t.sleep(2)
        pyxel.quit()


def draw():
    pyxel.cls(5)
    # presonnages
    pyxel.blt(p1.position['x'], p1.position['y'], img=0, u=0, v=0, w=6, h=8)
    pyxel.blt(p2.position['x'], p2.position['y'], img=0, u=7, v=0, w=6, h=8)

    # kunais
    pyxel.blt(p2.pos_kunai['x'], p2.pos_kunai['y'], img=0, u=42, v=0, w=4, h=3)
    pyxel.blt(p1.pos_kunai['x'], p1.pos_kunai['y'], img=0, u=42, v=4, w=4, h=3)

    # coeurs
    graphiques.coeurs(p1.coeur, p2.coeur)

    # vie
    graphiques.vie(p1.vie, p2.vie)


pyxel.run(update, draw)

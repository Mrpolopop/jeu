import pyxel


class Player:

    def __init__(self, joueur, vitesse, vit_kunai, vit_ult):

        self.vie = 5
        self.position = {'x': 100, 'y': 100}
        self.vitesse = vitesse
        self.coeur = 3
        self.pos_kunai = {'x': -10, 'y': -10}
        self.pos_ult = {'x': -10, 'y': -10}
        self.vit_kunai = vit_kunai
        self.vit_ult = vit_ult
        self.avancer = None
        self.reculer = None
        self.gauche = None
        self.droite = None
        self.attq = None
        self.ult = None
        self.joueur = joueur

        if joueur == 1:
            self.avancer = pyxel.KEY_Z
            self.reculer = pyxel.KEY_S
            self.droite = pyxel.KEY_D
            self.gauche = pyxel.KEY_Q
            self.attq = pyxel.KEY_A
            self.ult = pyxel.KEY_E
            self.position['x'] = 20

        elif joueur == 2:
            self.avancer = pyxel.KEY_KP_5
            self.reculer = pyxel.KEY_KP_2
            self.droite = pyxel.KEY_KP_3
            self.gauche = pyxel.KEY_KP_1
            self.attq = pyxel.KEY_KP_4
            self.ult = pyxel.KEY_KP_6

    def pos_update(self):

        if pyxel.btn(self.avancer):
            self.position['y'] -= self.vitesse

            if self.position['y'] <= 0:
                self.position['y'] = 0
                print(self.position['y'])

        if pyxel.btn(self.reculer):
            self.position['y'] += self.vitesse

            if self.position['y'] >= 121:
                self.position['y'] = 121
                print(128)

        if pyxel.btn(self.gauche):
            self.position['x'] -= self.vitesse

            if self.joueur == 1:

                if self.position['x'] <= 0:
                    self.position['x'] = 0

            elif self.joueur == 2:

                if self.position['x'] <= 64:
                    self.position['x'] = 64

        if pyxel.btn(self.droite):
            self.position['x'] += self.vitesse

            if self.joueur == 1:

                if self.position['x'] >= 58:
                    self.position['x'] = 58

            elif self.joueur == 2:

                if self.position['x'] >= 122:
                    self.position['x'] = 122

    def kunai_update(self):

        if self.joueur == 2:
            self.pos_kunai['x'] -= self.vit_kunai

        elif self.joueur == 1:
            self.pos_kunai['x'] += self.vit_kunai

        if pyxel.btn(self.attq):
            self.pos_kunai['x'] = self.position['x']
            self.pos_kunai['y'] = self.position['y']

    def ult_update(self):

        if self.joueur == 2:
            self.pos_ult['x'] -= self.vit_ult

        elif self.joueur == 1:
            self.pos_ult['x'] += self.vit_ult

        if pyxel.btn(self.ult):
            self.pos_ult['x'] = self.position['x']
            self.pos_ult['y'] = self.position['y']

    def vie_update(self, degats):

        self.vie -= degats

        if self.vie <= 0:

            self.coeur -= 1
            self.vie = 5


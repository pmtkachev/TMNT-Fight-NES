import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.life = {'life': 100, 'color': (0, 255, 0)}
        self.index = 0
        self.position = {'x': 0, 'y': 0}
        self.parameters = {'speed': 15, 'weight': 1}
        self.wright, self.wleft = False, False
        self.down, self.isjump = False, False
        self.fight_arm, self.fight_foot = False, False
        self.fight_arm_down, self.fight_foot_down = False, False
        self.block = False

    def jump(self):
        self.position['y'] -= (1 / 2) * self.parameters['weight'] * (self.parameters['speed'] ** 2)
        self.parameters['speed'] -= 5
        if self.parameters['speed'] < 0:
            self.parameters['weight'] = -1
        if self.parameters['speed'] == -20:
            self.isjump = False
            self.parameters['speed'] = 15
            self.parameters['weight'] = 1
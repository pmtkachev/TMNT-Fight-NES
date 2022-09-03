import pygame
from src.load_resources import sounds_fight


class Player(pygame.sprite.Sprite):
    def __init__(self, img, x, y, p_x, p_y, name, turtle=True):
        super().__init__()
        self.x, self.y, self.img = x, y, img
        self.turtle = turtle
        self.name = name
        self.life = {'life': 100, 'color': (0, 255, 0)}
        self.position = {'x': self.x, 'y': self.y}
        self.index = 0
        self.parameters = {'speed': 15, 'weight': 1}
        self.portrait = self.img['portrait']
        self.portrait_rect = self.portrait.get_rect()
        self.portrait_rect.x, self.portrait_rect.y = p_x, p_y
        self.image = self.img['stay'][self.index]
        self.rect = self.image.get_rect()
        self.wright, self.wleft = False, False
        self.down, self.isjump = False, False
        self.fight_arm, self.fight_foot = False, False
        self.fight_arm_down, self.fight_foot_down = False, False
        self.block, self.damage = False, False

    def jump(self):
        self.position['y'] -= (1 / 2) * self.parameters['weight'] * (self.parameters['speed'] ** 2)
        self.parameters['speed'] -= 5
        if self.parameters['speed'] < 0:
            self.parameters['weight'] = -1
        if self.parameters['speed'] == -20:
            self.isjump = False
            self.parameters['speed'] = 15
            self.parameters['weight'] = 1

    def update(self):

        self.index += 1
        if self.index >= len(self.img['stay']):
            self.index = 0
        self.image = self.img['stay'][self.index]


        # life status
        if self.life['life'] <= 60:
            self.life['color'] = (255, 255, 0)
        if self.life['life'] <= 30:
            self.life['color'] = (255, 0, 0)

        if self.wright and self.isjump:
            if self.index >= len(self.img['jump_flip']):
                self.index = 0
            self.image = self.img['jump_flip'][self.index]
            self.jump()
            self.position['x'] += 15
            if self.position['x'] >= 730:
                self.position['x'] -= 15
        elif self.wright:
            self.position['x'] += self.parameters['speed']
            self.image = self.img['wright'][self.index]
            if self.position['x'] >= 730:
                self.position['x'] -= self.parameters['speed']

        elif self.wleft and self.isjump:
            if self.index >= len(self.img['jump_flip']):
                self.index = 0
            self.image = self.img['jump_flip'][self.index]
            self.jump()
            self.position['x'] -= 15
            if self.position['x'] <= 70:
                self.position['x'] += 15
        elif self.wleft:
            self.position['x'] -= self.parameters['speed']
            self.image = self.img['wleft'][self.index]
            if self.position['x'] <= 70:
                self.position['x'] += self.parameters['speed']

        elif self.isjump and self.fight_arm:
            sounds_fight['fight_arm_sound'].play()
            self.image = self.img['arm_f_jump']
            self.fight_arm = False
        elif self.down and self.fight_arm:
            sounds_fight['fight_arm_sound'].play()
            self.image = self.img['arm_f_down']
            self.fight_arm = False

        elif self.isjump and self.fight_foot:
            sounds_fight['fight_foot_sound'].play()
            self.image = self.img['foot_f_jump']
            self.fight_foot = False
        elif self.down and self.fight_foot:
            sounds_fight['fight_foot_sound'].play()
            self.image = self.img['foot_f_down']
            self.fight_foot = False

        elif self.down and self.block:
            self.image = self.img['block_down']
        elif self.down:
            self.image = self.img['sit']
        elif self.isjump:
            self.image = self.img['jump']
            self.jump()

        elif self.fight_arm:
            sounds_fight['fight_arm_sound'].play()
            self.image = self.img['arm_f']
            self.fight_arm = False
        elif self.fight_foot:
            sounds_fight['fight_foot_sound'].play()
            self.image = self.img['foot_f']
            self.fight_foot = False
        elif self.block:
            self.image = self.img['block']
        if self.damage:
            self.image = self.img['damage']
            self.damage = False
        if self.life['life'] <= 0:
            self.image = self.img['defeat']

        self.rect = self.image.get_rect()
        if self.turtle:
            self.rect.x, self.rect.bottom = self.position['x'], self.position['y']
        else:
            self.rect.right, self.rect.bottom = self.position['x'], self.position['y']

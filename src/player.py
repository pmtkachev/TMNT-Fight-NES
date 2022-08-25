import pygame
import src.load_resources as lr


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.life = {'life': 100, 'color': (0, 255, 0)}
        self.position = {'x': 150, 'y': 310}
        self.index = 0
        self.parameters = {'speed': 15, 'weight': 1}
        self.portrait = lr.leo['portrait']
        self.portrait_rect = self.portrait.get_rect()
        self.portrait_rect.x, self.portrait_rect.y = 10, 10
        self.image = lr.leo['stay'][self.index]
        self.rect = self.image.get_rect()
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

    def update(self):
        self.rect = self.image.get_rect()
        self.index += 1
        if self.index >= len(lr.leo['stay']):
            self.index = 0
        self.image = lr.leo['stay'][self.index]
        self.rect.center = self.position['x'], self.position['y']

        # life status
        if self.life['life'] <= 60:
            self.life['color'] = (255, 255, 0)
        if self.life['life'] <= 30:
            self.life['color'] = (255, 0, 0)

        if self.wright and self.isjump:
            self.image = lr.leo['jump_flip'][self.index]
            self.jump()
            self.position['x'] += 15
            if self.position['x'] >= 730:
                self.position['x'] -= 15
        elif self.wright:
            self.position['x'] += self.parameters['speed']
            self.image = lr.leo['wright'][self.index]
            if self.position['x'] >= 730:
                self.position['x'] -= self.parameters['speed']

        elif self.wleft and self.isjump:
            self.image = lr.leo['jump_flip'][self.index]
            self.jump()
            self.position['x'] -= 15
            if self.position['x'] <= 70:
                self.position['x'] += 15
        elif self.wleft:
            self.position['x'] -= self.parameters['speed']
            self.image = lr.leo['wleft'][self.index]
            if self.position['x'] <= 70:
                self.position['x'] += self.parameters['speed']

        elif self.isjump and self.fight_arm:
            lr.sounds_fight['fight_arm_sound'].play()
            self.image = lr.leo['arm_f_jump']
            self.fight_arm = False
        elif self.down and self.fight_arm:
            lr.sounds_fight['fight_arm_sound'].play()
            self.image = lr.leo['arm_f_down']
            self.fight_arm = False

        elif self.isjump and self.fight_foot:
            lr.sounds_fight['fight_foot_sound'].play()
            self.image = lr.leo['foot_f_jump']
            self.fight_foot = False
        elif self.down and self.fight_foot:
            lr.sounds_fight['fight_foot_sound'].play()
            self.image = lr.leo['foot_f_down']
            self.fight_foot = False

        elif self.down and self.block:
            self.image = lr.leo['block_down']
        elif self.down:
            self.image = lr.leo['sit']
        elif self.isjump:
            self.image = lr.leo['jump']
            self.jump()

        elif self.fight_arm:
            lr.sounds_fight['fight_arm_sound'].play()
            self.image = lr.leo['arm_f']
            self.fight_arm = False
        elif self.fight_foot:
            lr.sounds_fight['fight_foot_sound'].play()
            self.image = lr.leo['foot_f']
            self.fight_foot = False
        elif self.block:
            self.image = lr.leo['block']

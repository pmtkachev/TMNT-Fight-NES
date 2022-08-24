import pygame
from src.player import fight_arm_sound, fight_foot_sound


class Shredder(pygame.sprite.Sprite):
    def __init__(self):
        super(Shredder, self).__init__()
        self.life = 100
        self.color_life = (0, 255, 0)
        self.portrait = pygame.image.load('img/sprites/enemies/shredder/shred_portrait.png')
        self.portrait_rect = self.portrait.get_rect()
        self.portrait_rect.x, self.portrait_rect.y = 740, 10
        self.images = [pygame.image.load(f'img/sprites/enemies/shredder/shred_stay_{i}.png') for i in range(0, 3)]
        self.images_wright = [pygame.image.load(f'img/sprites/enemies/shredder/shred_wright_0.png'),
                              pygame.image.load(f'img/sprites/enemies/shredder/shred_wleft_1.png'),
                              pygame.image.load(f'img/sprites/enemies/shredder/shred_wleft_2.png')]
        self.images_wleft = [pygame.image.load(f'img/sprites/enemies/shredder/shred_wleft_{i}.png') for i in
                             range(0, 3)]
        self.image_sit = pygame.image.load(f'img/sprites/enemies/shredder/shred_down.png')
        self.image_jump = pygame.image.load(f'img/sprites/enemies/shredder/shred_jump.png')
        self.image_arm = pygame.image.load(f'img/sprites/enemies/shredder/shred_arm.png')
        self.image_arm_down = pygame.image.load(f'img/sprites/enemies/shredder/shred_arm_down.png')
        self.image_arm_jump = pygame.image.load(f'img/sprites/enemies/shredder/shred_arm_jump.png')
        self.image_foot = pygame.image.load(f'img/sprites/enemies/shredder/shred_foot.png')
        self.image_foot_down = pygame.image.load(f'img/sprites/enemies/shredder/shred_foot_down.png')
        self.image_foot_jump = pygame.image.load(f'img/sprites/enemies/shredder/shred_foot_jump.png')
        self.image_block = pygame.image.load(f'img/sprites/enemies/shredder/shred_block.png')
        self.image_block_down = pygame.image.load(f'img/sprites/enemies/shredder/shred_block_down.png')
        self.image_damage = pygame.image.load(f'img/sprites/enemies/shredder/shred_damage.png')
        self.image_defeat = pygame.image.load(f'img/sprites/enemies/shredder/shred_defeat.png')
        self.index = 0
        self.image = self.images[self.index]
        self.x, self.y = 650, 298
        self.rect = self.image.get_rect()
        self.speed, self.m = 15, 1
        self.wright, self.wleft = False, False
        self.down, self.isjump = False, False
        self.fight_arm, self.fight_foot = False, False
        self.fight_arm_down, self.fight_foot_down = False, False
        self.block = False
        self.uron = False

    def jump(self):
        self.y -= (1 / 2) * self.m * (self.speed ** 2)
        self.speed -= 5
        if self.speed < 0:
            self.m = -1
        if self.speed == -20:
            self.isjump = False
            self.speed = 15
            self.m = 1

    def update(self):
        self.rect = self.image.get_rect()
        self.index += 1
        if self.life <= 60:
            self.color_life = (255, 255, 0)
        if self.life <= 30:
            self.color_life = (255, 0, 0)
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.rect.center = self.x, self.y

        if self.wright and self.isjump:
            self.image = self.image_jump
            self.jump()
            self.x += 15
            if self.x >= 730:
                self.x -= 15
        elif self.wright:
            self.x += self.speed
            self.image = self.images_wright[self.index]
            if self.x >= 730:
                self.x -= self.speed

        elif self.wleft and self.isjump:
            self.image = self.image_jump
            self.jump()
            self.x -= 15
            if self.x <= 70:
                self.x += 15
        elif self.wleft:
            self.x -= self.speed
            self.image = self.images_wleft[self.index]
            if self.x <= 70:
                self.x += self.speed

        elif self.isjump and self.fight_arm:
            fight_arm_sound.play()
            self.image = self.image_arm_jump
            self.fight_arm = False

        elif self.down and self.fight_arm:
            fight_arm_sound.play()
            self.image = self.image_arm_down
            self.fight_arm = False
        elif self.isjump and self.fight_foot:
            fight_foot_sound.play()
            self.image = self.image_foot_jump
            self.fight_foot = False
        elif self.down and self.fight_foot:
            fight_foot_sound.play()
            self.image = self.image_foot_down
            self.fight_foot = False
        elif self.down and self.block:
            self.image = self.image_block_down
        elif self.down:
            self.image = self.image_sit
        elif self.isjump:
            self.image = self.image_jump
            self.jump()

        elif self.fight_arm:
            fight_arm_sound.play()
            self.image = self.image_arm
            self.fight_arm = False
        elif self.fight_foot:
            fight_foot_sound.play()
            self.image = self.image_foot
            self.fight_foot = False
        elif self.block:
            self.image = self.image_block
        if self.uron:
            self.image = self.image_damage
            self.uron = False
        if self.life <= 0:
            self.image = self.image_defeat

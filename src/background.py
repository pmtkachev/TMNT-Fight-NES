import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.image = pygame.image.load('img/backgrounds/zone_1.png')
        self.x, self.y = 400, 0
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.centerx = self.x

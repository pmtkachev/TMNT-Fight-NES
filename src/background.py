import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, area):
        super(Background, self).__init__()
        self.image = area
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.y = 0

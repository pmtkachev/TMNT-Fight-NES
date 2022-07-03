import pygame

leo = [pygame.image.load(f'img/sprites/turtles/leo_stay_{i}.png') for i in range(1, 4)]


class Leo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Leo, self).__init__()
        self.image = leo[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

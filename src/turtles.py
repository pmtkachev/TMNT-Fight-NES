import pygame


class Leo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Leo, self).__init__()
        self.images = [pygame.image.load(f'img/sprites/turtles/leo_stay_{i}.png') for i in range(1, 4)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

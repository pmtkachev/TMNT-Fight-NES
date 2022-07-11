import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.images = [pygame.image.load(f'img/sprites/turtles/leo_stay_{i}.png') for i in range(1, 4)]
        self.images_wright = [pygame.image.load(f'img/sprites/turtles/leo_wright_{i}.png') for i in range(1, 4)]
        self.images_wleft = [pygame.image.load(f'img/sprites/turtles/leo_wleft_{i}.png') for i in range(1, 4)]
        self.image_sit = pygame.image.load(f'img/sprites/turtles/leo_sit.png')
        self.image_jump = pygame.image.load(f'img/sprites/turtles/leo_jump.png')
        self.index = 0
        self.image = self.images[self.index]
        self.x, self.y = 150, 260
        self.rect = self.image.get_rect()
        self.speed, self.m = 15, 1
        self.wright, self.wleft = False, False
        self.down, self.isjump = False, False

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.rect.center = self.x, self.y
        if self.wright:
            if self.x <= 730:
                self.x += self.speed
                self.image = self.images_wright[self.index]
        elif self.wleft:
            if self.x >= 90:
                self.x -= self.speed
                self.image = self.images_wleft[self.index]
        elif self.down:
            self.image = self.image_sit
        elif self.isjump:
            self.image = self.image_jump
            self.y -= (1 / 2) * self.m * (self.speed ** 2)
            self.speed -= 5
            if self.speed < 0:
                self.m = -1

            if self.speed == -20:
                self.isjump = False
                self.speed = 15
                self.m = 1

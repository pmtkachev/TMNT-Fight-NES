import pygame
from pygame.locals import *
import sys
from src import turtles

pygame.init()

background = pygame.image.load('img/backgrounds/beach_bg.png')
screen = pygame.display.set_mode((800, 395))
screen.blit(background, (-400, -5))
sprites = pygame.sprite.Group()
leo = turtles.Leo(400, 150)
sprites.add(leo)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    sprites.draw(screen)
    pygame.display.flip()

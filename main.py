import pygame
from pygame.locals import *
import sys
from src import turtles

SCREEN_SIZE = (800, 395)
BACKGROUNDS = [pygame.image.load('img/backgrounds/beach_bg.png')]


def add_sprite(sprite_group, sprites):
    for sprite in sprites:
        sprite_group.add(sprite)


def screen_draw(screen, sprites_group):
    screen.blit(BACKGROUNDS[0], (-400, -5))
    sprites_group.draw(screen)
    pygame.display.update()


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    sprites_group = pygame.sprite.Group()
    leo = turtles.Leo(150, 220)
    sprites = [leo]
    add_sprite(sprites_group, sprites)

    while True:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        sprites_group.update()
        screen_draw(screen, sprites_group)


if __name__ == '__main__':
    run_game()

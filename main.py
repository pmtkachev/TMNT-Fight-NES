import pygame
from pygame.locals import *
import sys
from src.player import Player
from src.background import Background

SCREEN_SIZE = (800, 395)


def add_sprite(sprite_group, sprites):
    for sprite in sprites:
        sprite_group.add(sprite)


def screen_draw(screen, sprites_group):
    sprites_group.draw(screen)
    pygame.display.update()


def check_events(player, background):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if not player.isjump:
                if event.key == K_a:
                    player.wleft = True
                elif event.key == K_d:
                    player.wright = True
                elif event.key == K_s:
                    player.down = True
                elif event.key == K_w:
                    player.wright, player.wleft = False, False
                    player.down = False
                    player.isjump = True

        if event.type == KEYUP:
            if event.key == K_a:
                player.wleft = False
            elif event.key == K_d:
                player.wright = False
            elif event.key == K_s:
                player.down = False


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    sprites_group = pygame.sprite.Group()
    player = Player()
    background = Background()
    sprites = [background, player]
    add_sprite(sprites_group, sprites)

    while True:
        clock.tick(7)

        check_events(player, background)
        sprites_group.update()
        screen_draw(screen, sprites_group)


if __name__ == '__main__':
    run_game()

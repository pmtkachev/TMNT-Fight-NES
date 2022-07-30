import pygame
from pygame.locals import *
import sys


def check_events(player):
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
                    player.down = False
                    player.isjump = True
                elif event.key == K_SPACE:
                    player.block = True
                elif event.key == K_n:
                    player.fight_arm = True
                elif event.key == K_m:
                    player.fight_foot = True

        if event.type == KEYUP:
            if event.key == K_a:
                player.wleft = False
            elif event.key == K_d:
                player.wright = False
            elif event.key == K_s:
                player.down = False
            elif event.key == K_n:
                player.fight_arm = False
            elif event.key == K_m:
                player.fight_foot = False
            elif event.key == K_SPACE:
                player.block = False


def add_sprite(sprite_group, sprites):
    for sprite in sprites:
        sprite_group.add(sprite)


def screen_draw(screen, sprites_group):
    sprites_group.draw(screen)
    pygame.display.update()


def update_background(player, background):
    if player.x <= 75 and player.wleft:
        background.x += 20
    elif player.x >= 720 and player.wright:
        background.x -= 20
    if background.x == 0:
        background.x -= 20
    elif background.x == -720:
        background.x += 20

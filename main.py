import pygame
from src.player import Player
from src.background import Background
from src.game_func import *

SCREEN_SIZE = (800, 395)


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    sprites_group = pygame.sprite.Group()
    background = Background()
    player = Player()
    sprites = [background, player]
    add_sprite(sprites_group, sprites)

    while True:
        clock.tick(7)
        check_events(player)
        update_background(player, background)
        sprites_group.update()
        screen_draw(screen, sprites_group)


if __name__ == '__main__':
    run_game()

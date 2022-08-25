import pygame
import src.load_resources as lr
from src import game_func as gf
from src.player import Player
from src.shredder import Shredder
from src.background import Background

SCREEN_SIZE = (800, 430)
pygame.init()

# Choose area
area = lr.background_areas['zone_1']
area_music = lr.musics_areas['zone_1']


def run_game():
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(SCREEN_SIZE)
    sprites_group = pygame.sprite.Group()
    background = Background(area)
    player = Player()
    enemy = Shredder()
    sprites = [background, enemy, player]
    gf.add_sprite(sprites_group, sprites)
    seconds = 60
    # area_music.play()

    while True:
        clock.tick(7)
        gf.check_events(player, seconds, enemy)
        gf.detect_collision(player, enemy)
        gf.update_background(player, background, enemy)
        sprites_group.update()
        gf.screen_draw(window, sprites_group, player, seconds, enemy)
        seconds -= 0.13


if __name__ == '__main__':
    run_game()

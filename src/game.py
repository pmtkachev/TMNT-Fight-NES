import pygame
import src.load_resources as lr
from src import game_func as gf
from src.player import Player
from src.background import Background


def run_game(window):
    # Choose area
    area = lr.background_areas['zone_1']
    area_music = lr.musics_areas['zone_1']
    clock = pygame.time.Clock()
    sprites_group = pygame.sprite.Group()
    background = Background(area)
    turtle = Player(lr.leo, 150, 310, 10, 10)
    shredder = Player(lr.shredder, 650, 298, 740, 10)
    sprites = [background, shredder, turtle]
    gf.add_sprite(sprites_group, sprites)
    seconds = 60
    # area_music.play()

    while True:
        clock.tick(7)
        gf.check_events(turtle, seconds, shredder)
        gf.detect_collision(turtle, shredder)
        gf.update_background(turtle, background, shredder)
        sprites_group.update()
        gf.screen_draw(window, sprites_group, turtle, seconds, shredder)
        seconds -= 0.13


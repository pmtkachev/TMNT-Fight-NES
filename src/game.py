import pygame
import src.load_resources as lr
from src import game_func as gf
from src.player import Player
from src.background import Background


def run_game(window, area, name):
    # Choose area
    area_bg = lr.background_areas[area]
    area_music = lr.musics_areas[area]
    name = name
    turtle = lr.choose_turtle(name)
    clock = pygame.time.Clock()
    sprites_group = pygame.sprite.Group()
    background = Background(area_bg)
    turtle = Player(turtle, 150, 405, 10, 10, name.upper())
    shredder = Player(lr.shredder, 650, 405, 740, 10, 'SHREDDER', False)
    sprites = [background, shredder, turtle]
    gf.add_sprite(sprites_group, sprites)
    seconds = 60
    area_music.play()

    while True:
        clock.tick(7)
        gf.check_events(turtle, seconds, shredder)
        gf.update_background(turtle, background, shredder)
        sprites_group.update()
        gf.detect_collision(turtle, shredder)
        gf.screen_draw(window, sprites_group, turtle, seconds, shredder)
        seconds -= 0.13


import pygame
import src.load_resources as lr
from src import game_func as gf
from src.player import Player
from src.background import Background


def run_game(window, area, name):
    # Choose area
    area_bg = lr.background_areas[area]
    area_music = lr.musics_areas[area]
    turtle = lr.choose_turtle(name)
    clock = pygame.time.Clock()
    sprites_group = pygame.sprite.Group()
    background = Background(area_bg)
    turtle = Player(turtle, 150, 405, 10, 10, name.upper())
    enemy_ = Player(lr.shredder, 650, 405, 740, 10, 'SHREDDER', False)
    sprites = [background, enemy_, turtle]
    gf.add_sprite(sprites_group, sprites)
    seconds = 60
    area_music.play()

    while True:
        clock.tick(7)
        gf.player_control(turtle)
        gf.enemy_control_ai(enemy_, turtle)
        gf.update_background(turtle, background, enemy_)
        sprites_group.update()
        gf.detect_collision(turtle, enemy_)
        gf.screen_draw(window, sprites_group, turtle, seconds, enemy_)
        seconds -= 0.13

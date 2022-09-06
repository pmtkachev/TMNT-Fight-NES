import pygame
import src.game_func as gf
from src.game import run_game
import src.load_resources as lr

ch_area_rect = lr.other_images['ch_area'].get_rect()
ch_area_rect.center = (400, 215)

ch_turtle_rect = lr.other_images['ch_turtle'].get_rect()
ch_turtle_rect.center = (400, 215)


def select_turtle(window, area):
    while True:
        window.fill((0, 0, 0))
        window.blit(lr.other_images['ch_turtle'], ch_turtle_rect)
        name = gf.check_mouse('turtle')
        if name:
            run_game(window, area, name)
        pygame.display.update()


def select_area(window):
    while True:
        window.fill((0, 0, 0))
        window.blit(lr.other_images['ch_area'], ch_area_rect)
        area = gf.check_mouse('area')
        if area:
            select_turtle(window, area)
        pygame.display.update()

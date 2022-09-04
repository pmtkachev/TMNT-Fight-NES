import pygame
from pygame.locals import MOUSEBUTTONDOWN
from src.game import run_game
import src.load_resources as lr

ch_area_rect = lr.other_images['ch_area'].get_rect()
ch_area_rect.center = (400, 215)

ch_turtle_rect = lr.other_images['ch_turtle'].get_rect()
ch_turtle_rect.center = (400, 215)


def check_mouse(trigger):
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if trigger:
                if 53 <= pos[0] <= 181 and 133 <= pos[1] <= 182:
                    lr.other_sounds['menu_select'].play()
                    return 'water_front'
                elif 26 <= pos[0] <= 176 and 267 <= pos[1] <= 320:
                    lr.other_sounds['menu_select'].play()
                    return 'pirate_ship'
                elif 617 <= pos[0] <= 721 and 135 <= pos[1] <= 181:
                    lr.other_sounds['menu_select'].play()
                    return 'down_town'
                elif 645 <= pos[0] <= 772 and 294 <= pos[1] <= 314:
                    lr.other_sounds['menu_select'].play()
                    return 'sewer'
            else:
                if 200 <= pos[0] <= 269 and 180 <= pos[1] <= 250:
                    lr.other_sounds['menu_select'].play()
                    return 'leo'
                elif 309 <= pos[0] <= 378 and 180 <= pos[1] <= 250:
                    lr.other_sounds['menu_select'].play()
                    return 'raph'
                elif 419 <= pos[0] <= 489 and 180 <= pos[1] <= 250:
                    lr.other_sounds['menu_select'].play()
                    return 'mike'
                elif 528 <= pos[0] <= 599 and 180 <= pos[1] <= 250:
                    lr.other_sounds['menu_select'].play()
                    return 'don'


def select_turtle(window, area):
    while True:
        window.fill((0, 0, 0))
        window.blit(lr.other_images['ch_turtle'], ch_turtle_rect)
        name = check_mouse(False)
        if name:
            run_game(window, area, name)
        pygame.display.update()


def select_area(window):
    while True:
        window.fill((0, 0, 0))
        window.blit(lr.other_images['ch_area'], ch_area_rect)
        area = check_mouse(True)
        if area:
            select_turtle(window, area)
        pygame.display.update()

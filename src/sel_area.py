import pygame
import src.game_func as gf
from src.game import run_game
import src.load_resources as lr


def select_turtle(window, area):
    cur_pos_x = 186
    while True:
        window.fill((0, 0, 0))
        window.blits(blit_sequence=((lr.other_images['ch_turtle'], (200, 108)),
                     (lr.other_images['cursor_t'], (cur_pos_x, 166))))

        name = gf.check_menu(cur_pos=cur_pos_x, menu='turtle')

        match name:
            case 'right':
                if cur_pos_x == 516:
                    cur_pos_x = 186
                else:
                    cur_pos_x += 110
            case 'left':
                if cur_pos_x == 186:
                    cur_pos_x = 516
                else:
                    cur_pos_x -= 110
            case 'esc':
                break
            case 'leo'|'raph'|'don'|'mike':
                run_game(window, area, name)

        pygame.display.update()


def select_area(window):
    cur_pos_y = 100
    while True:
        window.fill((0, 0, 0))
        window.blits(blit_sequence=((lr.other_images['ch_area'], (26, 83)),
                                    (lr.other_images['cursor'], (90, cur_pos_y))))

        area = gf.check_menu(menu='area', cur_pos=cur_pos_y)

        match area:
            case 'up':
                if cur_pos_y == 100:
                    cur_pos_y = 283
                else:
                    cur_pos_y -= 61
            case 'down':
                if cur_pos_y == 283:
                    cur_pos_y = 100
                else:
                    cur_pos_y += 61
            case 'esc':
                break
            case 'water_front'|'down_town'|'pirate_ship'|'sewer':
                select_turtle(window, area)

        pygame.display.update()

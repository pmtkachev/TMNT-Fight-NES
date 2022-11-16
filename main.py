import sys
from time import sleep
import pygame
import src.load_resources as lr
import src.game_func as gf
from src.sel_area import select_area

pygame.init()

# set window
window = pygame.display.set_mode((800, 430), flags=pygame.NOFRAME)


def about_info():
    while True:
        window.blit(lr.other_images['about'], (40, 0))
        if gf.check_menu(menu='about') == 'esc':
            break
        pygame.display.update()


# run main menu
def run():
    cur_pos_y = 228
    while True:
        window.blits(blit_sequence=((lr.other_images['splash'], (0, 0)),
                     (lr.other_images['cursor'], (320, cur_pos_y))))

        action = gf.check_menu(cur_pos_y)

        match action:
            case 'down':
                if cur_pos_y == 369:
                    cur_pos_y = 228
                else:
                    cur_pos_y += 47
            case 'up':
                if cur_pos_y == 228:
                    cur_pos_y = 369
                else:
                    cur_pos_y -= 47
            case 'start':
                select_area(window)
            case 'about':
                about_info()
            case 'exit':
                sleep(0.7)
                pygame.quit()
                sys.exit(0)

        pygame.display.update()


if __name__ == '__main__':
    run()

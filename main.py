import sys
from time import sleep
import pygame
import src.load_resources as lr
import src.game_func as gf
from src.game import run_game

pygame.init()

# set window
window = pygame.display.set_mode((800, 430), flags=pygame.NOFRAME)

# create main menu
start = lr.fonts['menu_font'].render('Start', False, (255, 255, 255))
start_rect = start.get_rect()
start_rect.x, start_rect.y = 355, 240
exit_ = lr.fonts['menu_font'].render('Exit', False, (255, 255, 255))
exit_rect = exit_.get_rect()
exit_rect.x, exit_rect.y = 364, 340
about = lr.fonts['menu_font'].render('About', False, (255, 255, 255))
about_rect = about.get_rect()
about_rect.x, about_rect.y = 355, 290


# run main menu
def run():
    while True:
        pygame.display.update()
        window.blits(blit_sequence=((start, start_rect), (exit_, exit_rect),
                                    (about, about_rect), (lr.other_images['splash'], (225, 20))))
        action = gf.check_menu(start_rect, about_rect, exit_rect)
        if action == 'start':
            run_game(window)
        elif action == 'about':
            print('My telegram: @pmtkachev')
        elif action == 'exit':
            sleep(0.7)
            pygame.quit()
            sys.exit(0)


if __name__ == '__main__':
    run()

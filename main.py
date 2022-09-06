import sys
from time import sleep
import pygame
import src.load_resources as lr
import src.game_func as gf
from src.sel_area import select_area

pygame.init()

# set window
window = pygame.display.set_mode((800, 430), flags=pygame.NOFRAME)

# create main menu
start = lr.fonts['menu_font'].render('Start', False, (255, 255, 255))
exit_ = lr.fonts['menu_font'].render('Exit', False, (255, 255, 255))
about = lr.fonts['menu_font'].render('About', False, (255, 255, 255))


# create about menu
about_text = lr.fonts['menu_font'].render('By Pavel Tkachev (c) 2022', False, (255, 255, 255))
tg_text = lr.fonts['menu_font'].render('Telegram: @pmtkachev', False, (255, 255, 255))
email_text = lr.fonts['menu_font'].render('E-mail: pmtkachev@bk.ru', False, (255, 255, 255))
back_text = lr.fonts['menu_font'].render('< Back', False, (255, 255, 255))


def about_info():
    while True:
        window.blits(blit_sequence=((lr.other_images['about'], (40, 0)),
                                    (about_text, (70, 130)),
                                    (tg_text, (70, 180)),
                                    (email_text, (70, 230)),
                                    (back_text, (65, 375))))
        action = gf.check_mouse('about')
        if action == 'exit':
            break
        pygame.display.update()


# run main menu
def run():
    while True:
        window.fill((0, 0, 0))
        window.blits(blit_sequence=((start, (360, 235)), (exit_, (365, 335)),
                                    (about, (360, 285)), (lr.other_images['splash'], (225, 20))))
        action = gf.check_mouse('menu')
        if action == 'start':
            select_area(window)
        elif action == 'about':
            about_info()
        elif action == 'exit':
            sleep(0.7)
            pygame.quit()
            sys.exit(0)
        pygame.display.update()


if __name__ == '__main__':
    run()

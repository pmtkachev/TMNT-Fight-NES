import sys
from time import sleep
import pygame
import src.load_resources as lr
import src.game_func as gf
from src.game import run_game
from src.sel_area import select_area

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

# create about menu
about_text = lr.fonts['menu_font'].render('By Pavel Tkachev (c) 2022', False, (255, 255, 255))
about_text_rect = about_text.get_rect()
about_text_rect.center = (350, 150)
tg_text = lr.fonts['menu_font'].render('Telegram: @pmtkachev', False, (255, 255, 255))
tg_text_rect = tg_text.get_rect()
tg_text_rect.center = (350, 200)
email_text = lr.fonts['menu_font'].render('E-mail: pmtkachev@bk.ru', False, (255, 255, 255))
email_text_rect = email_text.get_rect()
email_text_rect.center = (350, 250)
back_text = lr.fonts['menu_font'].render('< Back', False, (255, 255, 255))
back_text_rect = back_text.get_rect()
back_text_rect.center = (150, 400)


def about_info():
    while True:
        window.blits(blit_sequence=((lr.other_images['about'], (40, 0)),
                                    (about_text, about_text_rect),
                                    (tg_text, tg_text_rect),
                                    (email_text, email_text_rect),
                                    (back_text, back_text_rect)))
        action = gf.check_menu(pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0), back_text_rect)
        if action == 'exit':
            break
        pygame.display.update()


# run main menu
def run():
    while True:
        window.fill((0, 0, 0))
        window.blits(blit_sequence=((start, start_rect), (exit_, exit_rect),
                                    (about, about_rect), (lr.other_images['splash'], (225, 20))))
        action = gf.check_menu(start_rect, about_rect, exit_rect)
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

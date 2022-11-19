import pygame
from main import main_menu
import src.load_resources as lr
from random import randint


def up_down(event, cur_pos):
    if event.key == pygame.K_UP:
        lr.other_sounds['menu_selectel'].play()
        return 'up'
    if event.key == pygame.K_DOWN:
        lr.other_sounds['menu_selectel'].play()
        return 'down'
    if event.key == pygame.K_SPACE:
        lr.other_sounds['menu_select'].play()
        match cur_pos:
            case 228:
                return 'start'
            case 275:
                return 'help'
            case 322:
                return 'about'
            case 369:
                return 'exit'
            case 100:
                return 'water_front'
            case 161:
                return 'down_town'
            case 222:
                return 'pirate_ship'
            case 283:
                return 'sewer'


def check_menu(cur_pos=0, menu='main'):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            match menu:
                case 'main':
                    return up_down(event, cur_pos)
                case 'about':
                    if event.key == pygame.K_ESCAPE:
                        lr.other_sounds['menu_select'].play()
                        return 'esc'
                case 'area':
                    if event.key == pygame.K_ESCAPE:
                        lr.other_sounds['menu_select'].play()
                        return 'esc'
                    return up_down(event, cur_pos)
                case 'turtle':
                    if event.key == pygame.K_RIGHT:
                        lr.other_sounds['menu_selectel'].play()
                        return 'right'
                    if event.key == pygame.K_LEFT:
                        lr.other_sounds['menu_selectel'].play()
                        return 'left'
                    if event.key == pygame.K_SPACE:
                        lr.other_sounds['menu_select'].play()
                        match cur_pos:
                            case 186:
                                return 'leo'
                            case 296:
                                return 'raph'
                            case 406:
                                return 'mike'
                            case 516:
                                return 'don'

                    if event.key == pygame.K_ESCAPE:
                        lr.other_sounds['menu_select'].play()
                        return 'esc'


# check events
def player_control(player):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.stop()
                main_menu()

            if not player.isjump:
                if event.key == pygame.K_a:
                    player.wleft = True
                if event.key == pygame.K_d:
                    player.wright = True
                if event.key == pygame.K_s:
                    player.down = True

            if event.key == pygame.K_w:
                lr.sounds_fight['jump_sound'].play()
                player.down = False
                player.isjump = True
            elif event.key == pygame.K_SPACE:
                player.block = True
            elif event.key == pygame.K_o:
                player.fight_arm = True
            elif event.key == pygame.K_p:
                player.fight_foot = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.wleft = False
            if event.key == pygame.K_d:
                player.wright = False
            if event.key == pygame.K_s:
                player.down = False
            if event.key == pygame.K_SPACE:
                player.block = False


def enemy_control_ai(enemy, player):
    rect_right = player.rect.right + randint(20, 40)

    if enemy.rect.left >= rect_right:
        enemy.wleft, enemy.wright = True, False
    else:
        enemy.wright, enemy.wleft = True, False

    if -20 <= (enemy.rect.left - rect_right) <= 20:
        enemy.attack()


# add sprites in group
def add_sprite(sprite_group, sprites):
    for sprite in sprites:
        sprite_group.add(sprite)


def draw_lives(player, screen, enemy):
    pygame.draw.rect(screen, player.life['color'], (70, 42, player.life['life'] * 1.75, 10))
    shredder_rect = pygame.Rect(0, 42, enemy.life['life'] * 1.75, 10)
    shredder_rect.right = 730
    pygame.draw.rect(screen, enemy.life['color'], shredder_rect)


# draw screen
def screen_draw(window, sprites_group, player, seconds, enemy):
    sprites_group.draw(window)
    time = lr.fonts['time_font'].render(str(int(seconds)).zfill(2), False, (255, 255, 255))
    name_player = lr.fonts['name_font'].render(player.name, False, (255, 255, 255))
    name_enemy = lr.fonts['name_font'].render(enemy.name, False, (255, 255, 255))
    window.blits(blit_sequence=((lr.other_images['hud'], (10, 10, 175, 50)), (player.portrait, player.portrait_rect),
                                (enemy.portrait, enemy.portrait_rect), (time, (373, 5)),
                                (name_player, (70, 20)), (name_enemy, (660, 20))))
    draw_lives(player, window, enemy)

    pygame.display.update()


# update background
def update_background(player, background, enemy):
    if (player.position['x'] <= 75 and player.wleft) or (enemy.position['x'] <= 80 and enemy.wleft):
        background.rect.centerx += 20
    elif (player.position['x'] >= 720 and player.wright) or (enemy.position['x'] >= 720 and enemy.wright):
        background.rect.centerx -= 20
    if background.rect.centerx >= 640:
        background.rect.centerx -= 20
    elif background.rect.centerx <= 160:
        background.rect.centerx += 20

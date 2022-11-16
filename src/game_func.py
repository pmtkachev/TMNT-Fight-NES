import pygame
from main import run
import src.load_resources as lr
from pygame.locals import *


def up_down(event, cur_pos):
    if event.key == K_UP:
        lr.other_sounds['menu_selectel'].play()
        return 'up'
    if event.key == K_DOWN:
        lr.other_sounds['menu_selectel'].play()
        return 'down'
    if event.key == K_SPACE:
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
        if event.type == KEYDOWN:
            match menu:
                case 'main':
                    return up_down(event, cur_pos)
                case 'about':
                    if event.key == K_ESCAPE:
                        lr.other_sounds['menu_select'].play()
                        return 'esc'
                case 'area':
                    if event.key == K_ESCAPE:
                        lr.other_sounds['menu_select'].play()
                        return 'esc'
                    return up_down(event, cur_pos)
                case 'turtle':
                    if event.key == K_RIGHT:
                        lr.other_sounds['menu_selectel'].play()
                        return 'right'
                    if event.key == K_LEFT:
                        lr.other_sounds['menu_selectel'].play()
                        return 'left'
                    if event.key == K_SPACE:
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

                    if event.key == K_ESCAPE:
                        lr.other_sounds['menu_select'].play()
                        return 'esc'


# check events
def check_events(player, seconds, enemy):
    # if seconds <= 0:
    #     print('Game over')
    #     pygame.quit()
    #     sys.exit(0)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.mixer.stop()
                run()
            if event.key == K_w:
                lr.sounds_fight['jump_sound'].play()
                player.down = False
                player.isjump = True
            elif event.key == K_SPACE:
                player.block = True
            elif event.key == K_n:
                player.fight_arm = True
            elif event.key == K_m:
                player.fight_foot = True

            if event.key == K_UP:
                enemy.down = False
                lr.sounds_fight['jump_sound'].play()
                enemy.isjump = True
            elif event.key == K_c:
                enemy.block = True
            elif event.key == K_z:
                enemy.fight_arm = True
            elif event.key == K_x:
                enemy.fight_foot = True

            if not player.isjump:
                if event.key == K_a:
                    player.wleft = True
                if event.key == K_d:
                    player.wright = True
                if event.key == K_s:
                    player.down = True

            if not enemy.isjump:
                if event.key == K_LEFT:
                    enemy.wleft = True
                elif event.key == K_RIGHT:
                    enemy.wright = True
                elif event.key == K_DOWN:
                    enemy.down = True

        if event.type == KEYUP:
            if event.key == K_a:
                player.wleft = False
            if event.key == K_d:
                player.wright = False
            if event.key == K_s:
                player.down = False
            if event.key == K_n:
                player.fight_arm = False
            if event.key == K_m:
                player.fight_foot = False
            if event.key == K_SPACE:
                player.block = False

            if event.key == K_LEFT:
                enemy.wleft = False
            if event.key == K_RIGHT:
                enemy.wright = False
            if event.key == K_DOWN:
                enemy.down = False
            if event.key == K_1:
                enemy.fight_arm = False
            if event.key == K_2:
                enemy.fight_foot = False
            if event.key == K_c:
                enemy.block = False


# add sprites in group
def add_sprite(sprite_group, sprites):
    for sprite in sprites:
        sprite_group.add(sprite)


def detect_collision(player, enemy):
    collide = player.rect.colliderect(enemy.rect)
    if collide and player.wright:
        enemy.position['x'] += 15
    elif collide and player.fight_arm:
        enemy.damage = True
        enemy.life['life'] -= 3
    elif collide and player.fight_foot:
        enemy.damage = True
        enemy.life['life'] -= 5
    elif collide and player.fight_arm_down:
        enemy.damage = True
        enemy.life['life'] -= 4


def draw_lives(player, screen, shredder):
    pygame.draw.rect(screen, player.life['color'], (70, 42, player.life['life'] * 1.75, 10))
    shredder_rect = Rect(0, 42, shredder.life['life'] * 1.75, 10)
    shredder_rect.right = 730
    pygame.draw.rect(screen, shredder.life['color'], shredder_rect)


# draw screen
def screen_draw(window, sprites_group, player, seconds, shredder):
    sprites_group.draw(window)
    time = lr.fonts['time_font'].render(str(int(seconds)).zfill(2), False, (255, 255, 255))
    name_player = lr.fonts['name_font'].render(player.name, False, (255, 255, 255))
    name_enemy = lr.fonts['name_font'].render(shredder.name, False, (255, 255, 255))
    window.blits(blit_sequence=((lr.other_images['hud'], (10, 10, 175, 50)), (player.portrait, player.portrait_rect),
                                (shredder.portrait, shredder.portrait_rect), (time, (373, 5)),
                                (name_player, (70, 20)), (name_enemy, (660, 20))))
    draw_lives(player, window, shredder)
    pygame.draw.rect(window, (0, 255, 0), player.rect)
    pygame.draw.rect(window, (255, 0, 0), shredder.rect)
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

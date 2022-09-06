import sys
import pygame
from main import run
import src.load_resources as lr
from pygame.locals import *


def check_mouse(trigger):
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if trigger == 'area':
                if 55 <= pos[0] <= 180 and 135 <= pos[1] <= 180:
                    lr.other_sounds['menu_select'].play()
                    return 'water_front'
                elif 25 <= pos[0] <= 175 and 265 <= pos[1] <= 320:
                    lr.other_sounds['menu_select'].play()
                    return 'pirate_ship'
                elif 615 <= pos[0] <= 720 and 135 <= pos[1] <= 180:
                    lr.other_sounds['menu_select'].play()
                    return 'down_town'
                elif 645 <= pos[0] <= 770 and 295 <= pos[1] <= 315:
                    lr.other_sounds['menu_select'].play()
                    return 'sewer'
            elif trigger == 'turtle':
                if 200 <= pos[0] <= 270 and 180 <= pos[1] <= 250:
                    lr.other_sounds['menu_select'].play()
                    return 'leo'
                elif 310 <= pos[0] <= 380 and 180 <= pos[1] <= 250:
                    lr.other_sounds['menu_select'].play()
                    return 'raph'
                elif 420 <= pos[0] <= 490 and 180 <= pos[1] <= 250:
                    lr.other_sounds['menu_select'].play()
                    return 'mike'
                elif 530 <= pos[0] <= 600 and 180 <= pos[1] <= 250:
                    lr.other_sounds['menu_select'].play()
                    return 'don'
            elif trigger == 'menu':
                if 360 <= pos[0] <= 445 and 240 <= pos[1] <= 265:
                    lr.other_sounds['menu_select'].play()
                    return 'start'
                elif 360 <= pos[0] <= 445 and 290 <= pos[1] <= 310:
                    lr.other_sounds['menu_select'].play()
                    return 'about'
                elif 365 <= pos[0] <= 430 and 340 <= pos[1] <= 365:
                    lr.other_sounds['menu_select'].play()
                    return 'exit'
            elif trigger == 'about':
                if 65 <= pos[0] <= 165 and 380 <= pos[1] <= 405:
                    lr.other_sounds['menu_select'].play()
                    return 'exit'


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

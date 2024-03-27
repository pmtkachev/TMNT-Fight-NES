import pygame
from threading import Thread

import src.load_resources as lr
from main import main_menu


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
    if pygame.sprite.collide_mask(enemy, player):
        enemy.position['x'] += 20
        player.position['x'] -= 20
    distance = enemy.rect.left - player.rect.right
    if (distance > 15 and enemy.life['life'] >= 50) or \
            distance > 15 and player.life['life'] <= 50:
        enemy.wleft = True
    elif distance <= 15:
        enemy.wleft = False
    elif enemy.life['life'] <= 50:
        enemy.wright = True
        enemy.wleft = False
    if enemy.position['x'] >= 700:
        enemy.position['x'] -= enemy.parameters['speed']
    if distance <= 15:
        Thread(target=enemy.attack, daemon=True).start()


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

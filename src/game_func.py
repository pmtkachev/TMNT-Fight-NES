import pygame
from pygame.locals import *
import sys

# add sound, font, HUD
hud = pygame.image.load('img/sprites/hud.png')
pygame.font.init()
font = pygame.font.Font('fnt/pixel.ttf', 52)
font_name = pygame.font.Font('fnt/pixel.ttf', 16)
jump_sound = pygame.mixer.Sound('snd/jump.mp3')


# check events
def check_events(player, seconds, enemy):
    if seconds <= 0:
        print('Game over')
        pygame.quit()
        sys.exit(0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == KEYDOWN:
            if event.key == K_x:
                player.life -= 10
                # enemy.life -= 10
            if event.key == K_w:
                player.down = False
                jump_sound.play()
                player.isjump = True
            elif event.key == K_SPACE:
                player.block = True
            elif event.key == K_n:
                player.fight_arm = True
            elif event.key == K_m:
                player.fight_foot = True

            if event.key == K_UP:
                enemy.down = False
                jump_sound.play()
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


def draw_lives(player, screen, shredder):

    pygame.draw.rect(screen, player.color_life, (70, 42, player.life * 1.75, 10))
    shredder_rect = Rect(0, 42, shredder.life * 1.75, 10)
    shredder_rect.right = 730
    pygame.draw.rect(screen, shredder.color_life, shredder_rect)


# draw screen
def screen_draw(screen, sprites_group, player, seconds, shredder):
    sprites_group.draw(screen)
    time = font.render(str(int(seconds)).zfill(2), False, (255, 255, 255))
    name_player = font_name.render('LEO', False, (255, 255, 255))
    name_enemy = font_name.render('SHREDDER', False, (255, 255, 255))
    screen.blits(blit_sequence=((hud, (10, 10, 175, 50)), (player.portrait, player.portrait_rect),
                                (shredder.portrait, shredder.portrait_rect), (time, (373, 5)),
                                (name_player, (70, 20)), (name_enemy, (660, 20))))
    draw_lives(player, screen, shredder)
    pygame.display.update()


# update background
def update_background(player, background, enemy):
    if (player.x <= 75 and player.wleft) or (enemy.x <= 80 and enemy.wleft):
        background.x += 20
    elif (player.x >= 720 and player.wright) or (enemy.x >= 720 and enemy.wright):
        background.x -= 20
    if background.x >= 640:
        background.x -= 20
    elif background.x <= 160:
        background.x += 20

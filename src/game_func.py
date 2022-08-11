import pygame
from pygame.locals import *
import sys

# add sound, font, HUD
hud = pygame.image.load('img/sprites/hud.png')
pygame.font.init()
font = pygame.font.Font(None, 72)
jump_sound = pygame.mixer.Sound('snd/jump.mp3')


# check events
def check_events(player, seconds):
    if seconds <= 0:
        print('Game over')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_x:
                player.life -= 1
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

            if not player.isjump:
                if event.key == K_a:
                    player.wleft = True
                elif event.key == K_d:
                    player.wright = True
                elif event.key == K_s:
                    player.down = True

        if event.type == KEYUP:
            if event.key == K_a:
                player.wleft = False
            elif event.key == K_d:
                player.wright = False
            elif event.key == K_s:
                player.down = False
            elif event.key == K_n:
                player.fight_arm = False
            elif event.key == K_m:
                player.fight_foot = False
            elif event.key == K_SPACE:
                player.block = False


# add sprites in group
def add_sprite(sprite_group, sprites):
    for sprite in sprites:
        sprite_group.add(sprite)


# draw life
def draw_lives(player, screen):
    life_img = pygame.image.load('img/sprites/life_bar.png')
    for life in range(player.life):
        life_img_rect = life_img.get_rect()
        life_img_rect.x = 70 + 11 * life
        life_img_rect.y = 30
        screen.blit(life_img, life_img_rect)


# draw screen
def screen_draw(screen, sprites_group, player, seconds, shredder):
    sprites_group.draw(screen)
    screen.blit(hud, (10, 10, 175, 50))
    draw_lives(player, screen)
    screen.blit(player.portrait, player.portrait_rect)
    screen.blit(shredder.portrait, shredder.portrait_rect)
    text = font.render(str(int(seconds)).zfill(2), False, (255, 255, 255))
    screen.blit(text, (373, 13))
    pygame.display.update()


# update background
def update_background(player, background):
    if player.x <= 75 and player.wleft:
        background.x += 20
    elif player.x >= 720 and player.wright:
        background.x -= 20
    if background.x >= 640:
        background.x -= 20
    elif background.x <= 160:
        background.x += 20

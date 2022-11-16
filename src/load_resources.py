import pygame

pygame.mixer.init()
pygame.font.init()

# Load sounds
# Musics areas
musics_areas = {'sewer': pygame.mixer.Sound('snd/sewer.mp3'),
                'water_front': pygame.mixer.Sound('snd/water_front.mp3'),
                'pirate_ship': pygame.mixer.Sound('snd/pirate_ship.mp3'),
                'down_town': pygame.mixer.Sound('snd/down_town.mp3')}
sounds_fight = {'fight_arm_sound': pygame.mixer.Sound('snd/fight_arm.mp3'),
                'fight_foot_sound': pygame.mixer.Sound('snd/fight_foot.mp3'),
                'jump_sound': pygame.mixer.Sound('snd/jump.mp3')}
other_sounds = {'menu_select': pygame.mixer.Sound('snd/menu_select.mp3'),
                'menu_selectel': pygame.mixer.Sound('snd/menu_selectel.mp3')}

background_areas = {'sewer': pygame.image.load('img/backgrounds/sewer.png'),
                    'water_front': pygame.image.load('img/backgrounds/water_front.png'),
                    'pirate_ship': pygame.image.load('img/backgrounds/pirate_ship.png'),
                    'down_town': pygame.image.load('img/backgrounds/down_town.png')}


# Images turtles
def choose_turtle(turtle_name):
    turtle = {'portrait': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_portrait.png'),
              'stay': [pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_stay_{i}.png') for i in
                       range(1, 4)],
              'wright': [pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_wright_{i}.png') for i in
                         range(1, 4)],
              'wleft': [pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_wleft_{i}.png') for i in
                        range(1, 4)],
              'sit': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_sit.png'),
              'jump': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_jump.png'),
              'jump_flip': [pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_jump_flip_{i}.png') for
                            i in range(0, 3)],
              'arm_f': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_arm.png'),
              'arm_f_down': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_arm_down.png'),
              'arm_f_jump': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_arm_jump.png'),
              'foot_f': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_foot.png'),
              'foot_f_down': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_foot_down.png'),
              'foot_f_jump': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_foot_jump.png'),
              'block': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_block.png'),
              'block_down': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_block_down.png'),
              'damage': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_damage.png'),
              'defeat': pygame.image.load(f'img/sprites/turtles/{turtle_name}/{turtle_name}_defeat.png')}
    return turtle


# Enemies images
shredder = {'portrait': pygame.image.load('img/sprites/enemies/shredder/shred_portrait.png'),
            'stay': [pygame.image.load(f'img/sprites/enemies/shredder/shred_stay_{i}.png') for i in range(0, 3)],
            'wright': [pygame.image.load('img/sprites/enemies/shredder/shred_wright_0.png'),
                       pygame.image.load('img/sprites/enemies/shredder/shred_wleft_1.png'),
                       pygame.image.load('img/sprites/enemies/shredder/shred_wleft_2.png')],
            'wleft': [pygame.image.load(f'img/sprites/enemies/shredder/shred_wleft_{i}.png') for i in range(0, 3)],
            'sit': pygame.image.load('img/sprites/enemies/shredder/shred_down.png'),
            'jump': pygame.image.load('img/sprites/enemies/shredder/shred_jump.png'),
            'jump_flip': [pygame.image.load('img/sprites/enemies/shredder/shred_jump.png')],
            'arm_f': pygame.image.load('img/sprites/enemies/shredder/shred_arm.png'),
            'arm_f_down': pygame.image.load('img/sprites/enemies/shredder/shred_arm_down.png'),
            'arm_f_jump': pygame.image.load('img/sprites/enemies/shredder/shred_arm_jump.png'),
            'foot_f': pygame.image.load('img/sprites/enemies/shredder/shred_foot.png'),
            'foot_f_down': pygame.image.load('img/sprites/enemies/shredder/shred_foot_down.png'),
            'foot_f_jump': pygame.image.load('img/sprites/enemies/shredder/shred_foot_jump.png'),
            'block': pygame.image.load('img/sprites/enemies/shredder/shred_block.png'),
            'block_down': pygame.image.load('img/sprites/enemies/shredder/shred_block_down.png'),
            'damage': pygame.image.load('img/sprites/enemies/shredder/shred_damage.png'),
            'defeat': pygame.image.load('img/sprites/enemies/shredder/shred_defeat.png')}
other_images = {'hud': pygame.image.load('img/sprites/hud.png'),
                'splash': pygame.image.load('img/sprites/splash.png'),
                'about': pygame.image.load('img/sprites/about.png'),
                'ch_area': pygame.image.load('img/sprites/ch_area.png'),
                'ch_turtle': pygame.image.load('img/sprites/ch_turtle.png'),
                'cursor': pygame.image.load('img/sprites/cursor.png'),
                'cursor_t': pygame.image.load('img/sprites/cur_turt.png')}

# Fonts
fonts = {'time_font': pygame.font.Font('fnt/pixel.ttf', 52),
         'name_font': pygame.font.Font('fnt/pixel.ttf', 16)}

import pygame

pygame.mixer.init()
pygame.font.init()

# Load sounds
# Musics areas
musics_areas = {'zone_1': pygame.mixer.Sound('snd/music_1.mp3')}
sounds_fight = {'fight_arm_sound': pygame.mixer.Sound('snd/fight_arm.mp3'),
                'fight_foot_sound': pygame.mixer.Sound('snd/fight_foot.mp3'),
                'jump_sound': pygame.mixer.Sound('snd/jump.mp3')}
other_sounds = {'menu_select': pygame.mixer.Sound('snd/menu_select.mp3')}

# Load images
# Images areas
background_areas = {'zone_1': pygame.image.load('img/backgrounds/zone_1.png')}

# Images turtles
leo = {'portrait': pygame.image.load('img/sprites/turtles/leo/leo_portrait.png'),
       'stay': [pygame.image.load(f'img/sprites/turtles/leo/leo_stay_{i}.png') for i in range(1, 4)],
       'wright': [pygame.image.load(f'img/sprites/turtles/leo/leo_wright_{i}.png') for i in range(1, 4)],
       'wleft': [pygame.image.load(f'img/sprites/turtles/leo/leo_wleft_{i}.png') for i in range(1, 4)],
       'sit': pygame.image.load('img/sprites/turtles/leo/leo_sit.png'),
       'jump': pygame.image.load('img/sprites/turtles/leo/leo_jump.png'),
       'jump_flip': [pygame.image.load(f'img/sprites/turtles/leo/leo_jump_flip_{i}.png') for i in range(0, 3)],
       'arm_f': pygame.image.load('img/sprites/turtles/leo/leo_arm.png'),
       'arm_f_down': pygame.image.load('img/sprites/turtles/leo/leo_arm_down.png'),
       'arm_f_jump': pygame.image.load('img/sprites/turtles/leo/leo_arm_jump.png'),
       'foot_f': pygame.image.load('img/sprites/turtles/leo/leo_foot.png'),
       'foot_f_down': pygame.image.load('img/sprites/turtles/leo/leo_foot_down.png'),
       'foot_f_jump': pygame.image.load('img/sprites/turtles/leo/leo_foot_jump.png'),
       'block': pygame.image.load('img/sprites/turtles/leo/leo_block.png'),
       'block_down': pygame.image.load('img/sprites/turtles/leo/leo_block_down.png'),
       'damage': pygame.image.load('img/sprites/turtles/leo/leo_damage.png'),
       'defeat': pygame.image.load('img/sprites/turtles/leo/leo_defeat.png')}

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
                'splash': pygame.image.load('img/sprites/splash.png')}

# Fonts
fonts = {'time_font': pygame.font.Font('fnt/pixel.ttf', 52),
         'name_font': pygame.font.Font('fnt/pixel.ttf', 16),
         'menu_font': pygame.font.Font('fnt/pixel.ttf', 32)}

from src.player import Player
from src.shredder import Shredder
from src.background import Background
from src.game_func import *

SCREEN_SIZE = (800, 430)

# Choose area
area_music = pygame.mixer.Sound('snd/music_1.mp3')
area = pygame.image.load('img/backgrounds/zone_1.png')


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(SCREEN_SIZE)
    sprites_group = pygame.sprite.Group()
    background = Background(area)
    player = Player()
    enemy = Shredder()
    sprites = [background, enemy, player]
    add_sprite(sprites_group, sprites)
    seconds = 60
    area_music.play()

    while True:
        clock.tick(7)
        check_events(player, seconds, enemy)
        detect_collision(player, enemy)
        update_background(player, background, enemy)
        sprites_group.update()
        screen_draw(window, sprites_group, player, seconds, enemy)
        seconds -= 0.13


if __name__ == '__main__':
    run_game()

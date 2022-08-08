from src.player import Player
from src.background import Background
from src.game_func import *

SCREEN_SIZE = (800, 395)
music_1 = pygame.mixer.Sound('snd/music_1.mp3')


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    sprites_group = pygame.sprite.Group()
    background = Background()
    player = Player()
    sprites = [background, player]
    add_sprite(sprites_group, sprites)
    seconds = 60
    music_1.play()

    while True:
        clock.tick(7)
        check_events(player)
        update_background(player, background)
        sprites_group.update()
        screen_draw(screen, sprites_group, player, seconds)
        seconds -= 0.13


if __name__ == '__main__':
    run_game()

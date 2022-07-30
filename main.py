from src.player import Player
from src.background import Background
from src.game_func import *

SCREEN_SIZE = (800, 395)
leo_life = pygame.sprite.Sprite()
leo_life.image = pygame.image.load('img/sprites/turtles/leo/leo_life.png')
leo_life.rect = leo_life.image.get_rect()
leo_life.rect.x = 10
leo_life.rect.y = 10
life = pygame.sprite.Sprite()
life.image = pygame.image.load('img/sprites/life.png')
life.rect = life.image.get_rect()
life.rect.x = 88
life.rect.y = 10


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    sprites_group = pygame.sprite.Group()
    background = Background()
    player = Player()
    sprites = [background, player, leo_life, life]
    add_sprite(sprites_group, sprites)

    while True:
        clock.tick(7)
        check_events(player)
        update_background(player, background)
        sprites_group.update()
        screen_draw(screen, sprites_group)


if __name__ == '__main__':
    run_game()

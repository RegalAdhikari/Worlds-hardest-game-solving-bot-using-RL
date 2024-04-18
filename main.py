import pygame
from player import Player
from enemy import Enemy
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

screen_w = 1320
screen_h = 720
screen = pygame.display.set_mode((screen_w, screen_h))
tmx_data = load_pygame('Tiles/Level1.tmx')
sprite_group = pygame.sprite.Group()
isRunning = True
player = Player(140, 275, 37, 37)
enemy = Enemy(640, 285, 14, 14, True, False)
enemy2 = Enemy(640, 415, 14, 14, True, False)
enemy3 = Enemy(640, 350, 14, 14, True, False, False)
enemy4 = Enemy(640, 480, 14, 14, True, False, False)


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            pos = (x * 64, y * 64)
            Tile(pos=pos, surf=surf, groups=sprite_group)

for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        if layer.name == "Main":
            print("YOU HIT THE RED BLOCK!!")
            # for obj in layer:
            #     print(layer.name)
            #     if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(player.rect) == True:
            #         print("YOU HIT THE RED BLOCK!!")
            #         break


def update():
    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move(345, 935)
    enemy2.move(345, 935)
    enemy3.move(345, 935)
    enemy4.move(345, 935)


def draw():
    # screen.fill((181, 181, 252))
    screen.fill('white')
    sprite_group.draw(screen)
    player.draw(screen)
    enemy.draw(screen)
    enemy2.draw(screen)
    enemy3.draw(screen)
    enemy4.draw(screen)
    pygame.display.update()


while isRunning:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    update()
    draw()

pygame.quit()

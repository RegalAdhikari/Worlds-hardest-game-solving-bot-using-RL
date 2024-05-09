import sys
import pygame
from player import Player
from enemy import Enemy
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()
tile_rect = []
collider_rects = []  # List of tile colliders
screen_w = 1320
screen_h = 720
screen = pygame.display.set_mode((screen_w, screen_h))
tmx_data = load_pygame('Tiles/Level2.tmx')
sprite_group = pygame.sprite.Group()
isRunning = True
spawnpoint_x = 140
spawnpoint_y = 275
player = Player(spawnpoint_x, spawnpoint_y, 37, 37,5)
enemy = Enemy(350, 155, 14, 14, True, False)
enemy2 = Enemy(414, 484, 14, 14, True, False)
enemy3 = Enemy(478, 155, 14, 14, True, False, False, False)
enemy4 = Enemy(542, 484, 14, 14, True, False, False, False)
enemy5 = Enemy(606, 155, 14, 14, True, False, False, False)
enemy6 = Enemy(670, 484, 14, 14, True, False, False,False)
enemy7 = Enemy(734, 155, 14, 14, True, False, False, False)
enemy8 = Enemy(798, 484, 14, 14, True, False, False, False)
enemy9 = Enemy(862, 155, 14, 14, True, False, False, False)
enemy10 = Enemy(926, 484, 14, 14, True, False, False, False)
enemy11 = Enemy(990, 155, 14, 14, True, False, False, False)
enemy12 = Enemy(1054, 484, 14, 14, True, False, False, False)

color = (255, 0, 0)
redrect = pygame.Rect(1100, 260, 60, 120)
redrect.topleft = (1100, 260)


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        if layer.name == "Main":
            for x, y, surf in layer.tiles():
                pos = (x * 64, y * 64)
                Tile(pos=pos, surf=surf, groups=sprite_group)
                tile_rect.append(pygame.Rect(x * 64, y * 64, 64, 64))
                collider_rects.append(pygame.Rect(x * 64, y * 64, 64, 64))

for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            pos = (x * 64, y * 64)
            Tile(pos=pos, surf=surf, groups=sprite_group)

def update():
    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move2(155, 484)
    enemy2.move2(155, 484)
    enemy3.move2(155, 484)
    enemy4.move2(155, 484)
    enemy5.move2(155, 484)
    enemy6.move2(155, 484)
    enemy7.move2(155, 484)
    enemy8.move2(155, 484)
    enemy9.move2(155, 484)
    enemy10.move2(155, 484)
    enemy11.move2(155, 484)
    enemy12.move2(155, 484)
    collide = pygame.Rect.colliderect(player.rect1, enemy.rect2)
    if collide:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide2 = pygame.Rect.colliderect(player.rect1, enemy2.rect2)
    if collide2:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide3 = pygame.Rect.colliderect(player.rect1, enemy3.rect2)
    if collide3:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide4 = pygame.Rect.colliderect(player.rect1, enemy4.rect2)
    if collide4:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide5 = pygame.Rect.colliderect(player.rect1, enemy5.rect2)
    if collide5:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide6 = pygame.Rect.colliderect(player.rect1, enemy6.rect2)
    if collide6:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide7 = pygame.Rect.colliderect(player.rect1, enemy7.rect2)
    if collide7:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide8 = pygame.Rect.colliderect(player.rect1, enemy8.rect2)
    if collide8:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide9 = pygame.Rect.colliderect(player.rect1, enemy9.rect2)
    if collide9:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide10 = pygame.Rect.colliderect(player.rect1, enemy10.rect2)
    if collide10:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide11 = pygame.Rect.colliderect(player.rect1, enemy11.rect2)
    if collide11:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collide12 = pygame.Rect.colliderect(player.rect1, enemy12.rect2)
    if collide12:
        player.player_x = spawnpoint_x
        player.player_y = spawnpoint_y
    collidered = pygame.Rect.colliderect(player.rect1, redrect)
    if collidered:
        sys.exit()


def draw():
    # screen.fill((181, 181, 252))
    screen.fill('white')
    drawColliders()
    sprite_group.draw(screen)
    player.draw(screen)
    enemy.draw(screen)
    enemy2.draw(screen)
    enemy3.draw(screen)
    enemy4.draw(screen)
    enemy5.draw(screen)
    enemy6.draw(screen)
    enemy7.draw(screen)
    enemy8.draw(screen)
    enemy9.draw(screen)
    enemy10.draw(screen)
    enemy11.draw(screen)
    enemy12.draw(screen)
    
    pygame.draw.rect(screen, color, pygame.Rect(1100, 260, 60, 120), 2)
    pygame.display.update()


def drawColliders():
    index = 0
    for b in tile_rect:
        # To see the colliders simply uncomment the line below
        # pygame.draw.rect(screen, color, tile_rect[index])
        collideboundary = pygame.Rect.colliderect(player.rect1, collider_rects[index])
        if collideboundary:
            player.player_x = spawnpoint_x
            player.player_y = spawnpoint_y
        index = index + 1


while isRunning:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    update()
    draw()

pygame.quit()

import sys
import pygame
from player import Player
from enemy import Enemy
from pytmx.util_pygame import load_pygame
from enum import Enum


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Level1AI:
    def __init__(self):
        self.frame_iteration = 0
        pygame.init()
        self.screen_w = 1320
        self.screen_h = 720
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        self.tmx_data = load_pygame('Tiles/Level1.tmx')
        self.sprite_group = pygame.sprite.Group()
        self.is_running = True
        self.spawnpoint_x = 140
        self.spawnpoint_y = 275
        self.player = Player(self.spawnpoint_x, self.spawnpoint_y, 37, 37, 5)
        self.enemy = Enemy(640, 285, 14, 14, True, False)
        self.enemy2 = Enemy(640, 415, 14, 14, True, False)
        self.enemy3 = Enemy(640, 350, 14, 14, True, False, False)
        self.enemy4 = Enemy(640, 480, 14, 14, True, False, False)
        self.tile_rect = []
        self.enemyrect = pygame.Rect(self.enemy.player_x, self.enemy.player_y, 14, 14)
        self.collider_rects = []  # List of tile colliders
        self.color = (255, 0, 0)
        self.red_rect = pygame.Rect(1050, 200, 50, 50)
        self.red_rect.topleft = (1050, 200)

    class Tile(pygame.sprite.Sprite):
        def __init__(self, pos, surf, groups):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_rect(topleft=pos)

    def setup_tiles(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                if layer.name == "Main":
                    for x, y, surf in layer.tiles():
                        pos = (x * 64, y * 64)
                        self.Tile(pos=pos, surf=surf, groups=self.sprite_group)
                        self.tile_rect.append(pygame.Rect(x * 64, y * 64, 64, 64))
                        self.collider_rects.append(pygame.Rect(x * 64, y * 64, 64, 64))

        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 64, y * 64)
                    self.Tile(pos=pos, surf=surf, groups=self.sprite_group)
                    # tile_rect = pygame.Rect(x * 64, y * 64, 64, 64)

    def update(self):
        keys = pygame.key.get_pressed()

        self.enemy.move(345, 935)
        self.enemy2.move(345, 935)
        self.enemy3.move(345, 935)
        self.enemy4.move(345, 935)
        collide = pygame.Rect.colliderect(self.player.rect1, self.enemy.rect2)
        if collide:
            self.reset()
        collide2 = pygame.Rect.colliderect(self.player.rect1, self.enemy2.rect2)
        if collide2:
            self.reset()
        collide3 = pygame.Rect.colliderect(self.player.rect1, self.enemy3.rect2)
        if collide3:
            self.reset()
        collide4 = pygame.Rect.colliderect(self.player.rect1, self.enemy4.rect2)
        if collide4:
            self.reset()
        collidered = pygame.Rect.colliderect(self.player.rect1, self.red_rect)
        if collidered:
            sys.exit()
    def reset(self):
        self.player.player_x = self.spawnpoint_x
        self.player.player_y = self.spawnpoint_y
        self.frame_iteration = 0
    def drawColliders(self):
        index = 0
        for b in self.tile_rect:
            collideboundary = pygame.Rect.colliderect(self.player.rect1, self.collider_rects[index])
            if collideboundary:
                self.reset()
            index += 1

    def draw(self):
        self.screen.fill('white')
        self.sprite_group.draw(self.screen)
        self.drawColliders()
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.enemy2.draw(self.screen)
        self.enemy3.draw(self.screen)
        self.enemy4.draw(self.screen)
        pygame.draw.rect(self.screen, self.color, pygame.Rect(1050, 200, 60, 60), 2)
        # pygame.draw.rect(self.screen, self.color, pygame.Rect(self.enemy.player_x-14,self.enemy.player_y-14,28,28),2)
        pygame.display.update()

    def play_step(self, action):
        pygame.time.delay(50)
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
        self.update()
        self.draw()
        pygame.display.update()
        pygame.quit()

        self.player.move(action)


if __name__ == "__main__":
    game = Level1AI()
    game.setup_tiles()
    while game.is_running:
        game.play_step()

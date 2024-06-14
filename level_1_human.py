import os
import sys
import pygame
from player import Player
from enemy import Enemy
from pytmx.util_pygame import load_pygame


class level1:
    def __init__(self):
        pygame.init()
        self.islevel1 = True
        screen_w = 1320
        screen_h = 720
        self.screen = pygame.display.set_mode((screen_w, screen_h))
        self.tmx_data = load_pygame('Tiles/Level1.tmx')
        self.sprite_group = pygame.sprite.Group()
        self.is_Running = True
        self.spawnpoint_x = 140
        self.spawnpoint_y = 275
        self.player = Player(self.spawnpoint_x, self.spawnpoint_y, 37, 37,5)
        self.enemy = Enemy(346, 285, 14, 14, 5, (0, 0, 255))
        self.enemy2 = Enemy(346, 415, 14, 14, 5, (0, 0, 255))
        self.enemy3 = Enemy(934, 350, 14, 14, 5, (0, 0, 255))
        self.enemy4 = Enemy(934, 480, 14, 14, 5, (0, 0, 255))
        self.tile_rect = []
        self.collider_rects = []  # List of tile colliders
        self.color = (255, 0, 0)
        self.redrect = pygame.Rect(1050, 200, 50, 50)
        self.redrect.topleft = (1050, 200)


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
        self.player.move(keys)
        self.enemy.move(345, 935)
        self.enemy2.move(345, 935)
        self.enemy3.move(345, 935)
        self.enemy4.move(345, 935)
        collide = pygame.Rect.colliderect(self.player.rect1, self.enemy.rect2)
        if collide:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide2 = pygame.Rect.colliderect(self.player.rect1, self.enemy2.rect2)
        if collide2:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide3 = pygame.Rect.colliderect(self.player.rect1, self.enemy3.rect2)
        if collide3:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide4 = pygame.Rect.colliderect(self.player.rect1, self.enemy4.rect2)
        if collide4:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collidered = pygame.Rect.colliderect(self.player.rect1, self.redrect)
        if collidered:
            from mainscreen import main_screen
            self.islevel1 = False
            main_screen()



    def draw(self):
        if self.islevel1:
            # screen.fill((181, 181, 252))
            self.screen.fill('white')

            self.sprite_group.draw(self.screen)
            self.drawColliders()
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
            self.enemy2.draw(self.screen)
            self.enemy3.draw(self.screen)
            self.enemy4.draw(self.screen)

            pygame.draw.rect(self.screen, self.color, pygame.Rect(1050, 200, 60, 60), 2)
            pygame.display.update()


    def drawColliders(self):
        index = 0
        for b in self.tile_rect:
            # To see the colliders simply uncomment the line below
            # pygame.draw.rect(screen, color, tile_rect[index])
            collideboundary = pygame.Rect.colliderect(self.player.rect1, self.collider_rects[index])
            if collideboundary:
                self.player.player_x = self.spawnpoint_x
                self.player.player_y = self.spawnpoint_y
            index = index + 1


    def run(self):
        self.setup_tiles()
        while self.is_Running:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_Running = False
            self.update()
            self.draw()
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = level1()
    game.run()

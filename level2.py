import sys
import pygame
from player import Player
from enemy import Enemy
import pytmx
from pytmx.util_pygame import load_pygame
# from mainscreen import main_screen

class level2:
    def __init__(self):
        pygame.init()
        self.tile_rect = []
        self.collider_rects = []  # List of tile colliders
        self.islevel2 = True
        screen_w = 1320
        screen_h = 720
        self.screen = pygame.display.set_mode((screen_w, screen_h))
        self.tmx_data = load_pygame('Tiles/Level2.tmx')
        self.sprite_group = pygame.sprite.Group()
        self.is_Running = True
        self.spawnpoint_x = 140
        self.spawnpoint_y = 275
        self.player = Player(self.spawnpoint_x, self.spawnpoint_y, 37, 37, 5)
        self.enemy = Enemy(350, 155, 14, 14, 5, (0, 0, 255))
        self.enemy2 = Enemy(414, 484, 14, 14, 5, (0, 0, 255))
        self.enemy3 = Enemy(478, 155, 14, 14, 5, (0, 0, 255), False)
        self.enemy4 = Enemy(542, 484, 14, 14, 5, (0, 0, 255), False)
        self.enemy5 = Enemy(606, 155, 14, 14, 5, (0, 0, 255), False)
        self.enemy6 = Enemy(670, 484, 14, 14, 5, (0, 0, 255), False)
        self.enemy7 = Enemy(734, 155, 14, 14, 5, (0, 0, 255), False)
        self.enemy8 = Enemy(798, 484, 14, 14, 5, (0, 0, 255), False)
        self.enemy9 = Enemy(862, 155, 14, 14, 5, (0, 0, 255), False)
        self.enemy10 = Enemy(926, 484, 14, 14, 5, (0, 0, 255), False)
        self.enemy11 = Enemy(990, 155, 14, 14, 5, (0, 0, 255), False)
        self.enemy12 = Enemy(1054, 484, 14, 14, 5, (0, 0, 255), False)

        self.color = (255, 0, 0)
        self.red_rect = pygame.Rect(1100, 260, 60, 120)
        self.red_rect.topleft = (1100, 260)


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


    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        self.enemy.move2(155, 484)
        self.enemy2.move2(155, 484)
        self.enemy3.move2(155, 484)
        self.enemy4.move2(155, 484)
        self.enemy5.move2(155, 484)
        self.enemy6.move2(155, 484)
        self.enemy7.move2(155, 484)
        self.enemy8.move2(155, 484)
        self.enemy9.move2(155, 484)
        self.enemy10.move2(155, 484)
        self.enemy11.move2(155, 484)
        self.enemy12.move2(155, 484)
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
        collide5 = pygame.Rect.colliderect(self.player.rect1, self.enemy5.rect2)
        if collide5:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide6 = pygame.Rect.colliderect(self.player.rect1, self.enemy6.rect2)
        if collide6:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide7 = pygame.Rect.colliderect(self.player.rect1, self.enemy7.rect2)
        if collide7:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide8 = pygame.Rect.colliderect(self.player.rect1, self.enemy8.rect2)
        if collide8:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide9 = pygame.Rect.colliderect(self.player.rect1, self.enemy9.rect2)
        if collide9:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide10 = pygame.Rect.colliderect(self.player.rect1, self.enemy10.rect2)
        if collide10:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide11 = pygame.Rect.colliderect(self.player.rect1, self.enemy11.rect2)
        if collide11:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collide12 = pygame.Rect.colliderect(self.player.rect1, self.enemy12.rect2)
        if collide12:
            self.player.player_x = self.spawnpoint_x
            self.player.player_y = self.spawnpoint_y
        collidered = pygame.Rect.colliderect(self.player.rect1, self.red_rect)
        if collidered:
            from mainscreen import main_screen
            self.islevel2 = False
            main_screen()


    def draw(self):
        if self.islevel2:
            # screen.fill((181, 181, 252))
            self.screen.fill('white')
            self.drawColliders()
            self.sprite_group.draw(self.screen)
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
            self.enemy2.draw(self.screen)
            self.enemy3.draw(self.screen)
            self.enemy4.draw(self.screen)
            self.enemy5.draw(self.screen)
            self.enemy6.draw(self.screen)
            self.enemy7.draw(self.screen)
            self.enemy8.draw(self.screen)
            self.enemy9.draw(self.screen)
            self.enemy10.draw(self.screen)
            self.enemy11.draw(self.screen)
            self.enemy12.draw(self.screen)

            pygame.draw.rect(self.screen, self.color, pygame.Rect(1100, 260, 60, 120), 2)
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
    game = level2()
    game.run()
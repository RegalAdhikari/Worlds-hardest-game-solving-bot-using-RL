import pygame


class Enemy:
    def __init__(self, player_x, player_y, width, height, enemy_speed=25, color=(0, 0, 255), right=True, up=True):
        self.player_x = player_x
        self.player_y = player_y
        self.width = width
        self.height = height
        self.enemy_speed = 10
        self.color = color
        self.right = right
        self.up = up
        self.rect2 = pygame.Rect(player_x, player_y, 14, 14)
        self.rect2.topleft = (player_x, player_y)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.player_x, self.player_y), self.width, self.height)

    def move(self, bound_x1, bound_x2):
        if self.player_x < bound_x1 or self.player_x > bound_x2:
            self.right = not self.right
        if self.right:
            self.player_x += self.enemy_speed
            self.rect2.x = self.player_x
        else:
            self.player_x -= self.enemy_speed
            self.rect2.x = self.player_x

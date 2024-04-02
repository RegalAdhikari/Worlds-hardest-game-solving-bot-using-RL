import pygame


class Player:
    def __init__(self, player_x, player_y, width, height, player_speed=5, color=(255, 0, 0)):
        self.player_x = player_x
        self.player_y = player_y
        self.width = width
        self.height = height
        self.player_speed = player_speed
        self.color = color

    def move(self, keys):
        if keys[pygame.K_a] and self.player_x > 0:
            self.player_x -= self.player_speed
        if keys[pygame.K_d] and self.player_x < 800 - self.height:
            self.player_x += self.player_speed
        if keys[pygame.K_w] and self.player_y > 0:
            self.player_y -= self.player_speed
        if keys[pygame.K_s] and self.player_y < 600 - self.width:
            self.player_y += self.player_speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.player_x, self.player_y, self.width, self.height))

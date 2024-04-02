import pygame

from player import Player
from enemy import Enemy

pygame.init()

screen_w = 800
screen_h = 600
screen = pygame.display.set_mode((screen_w, screen_h))
isRunning = True
clock = pygame.time.Clock()
player = Player(50, 350, 15, 15)
enemy = Enemy(250, 300, 7, 7, True, False)
enemy2 = Enemy(250, 350, 7, 7, True, False)
enemy3 = Enemy(500, 325, 7, 7, True, False,False)
enemy4 = Enemy(500, 375, 7, 7, True, False,False)


def update():
    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move(250,500)
    enemy2.move(250, 500)
    enemy3.move(250,500)
    enemy4.move(250, 500)


def draw():
    screen.fill((181, 181, 252))
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

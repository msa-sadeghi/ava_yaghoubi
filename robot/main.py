import pygame
from player import Player
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
my_player = Player(100, 300)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_player.draw(screen)    
    pygame.display.update()
    clock.tick(FPS)
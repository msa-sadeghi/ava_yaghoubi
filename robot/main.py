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
    if my_player.moving:
        my_player.change_animation("Run")
    else:
        my_player.change_animation("Idle")
    
    screen.fill("lightblue")
    my_player.draw(screen)  
    my_player.move()  
    pygame.display.update()
    clock.tick(FPS)
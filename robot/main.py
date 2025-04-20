import pygame
from player import Player
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
my_player = Player(100, 300)
player_bullet_group = pygame.sprite.Group()
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_player.moving and my_player.shooting:
        my_player.change_animation("RunShoot")
    elif my_player.moving:
        my_player.change_animation("Run")
    elif my_player.slide:
        my_player.change_animation('Slide') 
    elif my_player.jump:
        my_player.change_animation('Jump') 
    elif my_player.shooting:
        my_player.change_animation('Shoot')
    else:
        my_player.change_animation("Idle")
    
    screen.fill("lightblue")
    my_player.draw(screen)  
    my_player.shoot(player_bullet_group)
    my_player.move()  
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
from config import *
from character import Character
clock = pygame.time.Clock()
pygame.init()

player = Character("player", 100, 300, 70, 10)
moving_left, moving_right = (False, False)
jumped = False
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                jumped = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
    screen.fill("black")            
    player.move(moving_left, moving_right)
    if moving_left or moving_right:
        player.change_action("Run") 
    else:
        player.change_action("Idle") 
        
    if jumped and player.in_air == False:
        player.in_air = True
        player.gravity = -15   
    if player.in_air:
        player.change_action("Jump")   
    player.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)
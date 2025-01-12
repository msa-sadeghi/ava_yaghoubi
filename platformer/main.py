from config import *
from character import Character
clock = pygame.time.Clock()
pygame.init()

player = Character("player", 100, 300, 70, 10)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
            
    player.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)
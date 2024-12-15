import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
paddle1 = pygame.Rect(10,HEIGHT//2 - 50, 20, 100)
ball = pygame.Rect(100,200, 30, 30)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle1.y -= 5
    if keys[pygame.K_DOWN]:
        paddle1.y += 5
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (115, 217, 111),paddle1)  
    pygame.draw.ellipse(screen, (255,255,255), ball)     
    pygame.display.update()
    clock.tick(FPS)
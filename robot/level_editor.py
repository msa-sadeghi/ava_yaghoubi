import pygame 
pygame.init()  # Initialize pygame
import os
WIDTH = 800
HEIGHT = 600
SIDE_MARGIN = 400
LOWER_MARGIN = 100
FPS = 60

tile_images =  []
tiles = os.listdir("game_world/Tiles")  # Number of tiles in the folder
for tile in tiles:
    tile_images.append(tile)  # Load the images
objects = os.listdir("game_world/Objects")  # Number of tiles in the folder
for obj in objects:
    tile_images.append(obj)  # Load the images

print(tile_images)

screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))   
pygame.display.set_caption("Level Editor")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")  
    pygame.draw.rect(screen, "lightblue", (WIDTH, 0, SIDE_MARGIN,HEIGHT + LOWER_MARGIN))  
    pygame.draw.rect(screen, "lightblue", (0, HEIGHT,WIDTH +  SIDE_MARGIN, HEIGHT)) 
    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Maintain the frame rate
pygame.quit()  # Quit pygame


import pygame 
from button import Button
pygame.init()  # Initialize pygame
import os
WIDTH = 800
HEIGHT = 600
SIDE_MARGIN = 600
LOWER_MARGIN = 100
FPS = 60

tile_images =  []
tiles = os.listdir("game_world/Tiles")  # Number of tiles in the folder
for tile in tiles:
    tile_images.append("game_world/Tiles/" +tile)  # Load the images

objects = os.listdir("game_world/Objects")  # Number of tiles in the folder
object_images =  []
for obj in objects:
    object_images.append("game_world/Objects/"+obj)  # Load the images

tile_btns = []
tile_row =0
tile_col = 0

for tile_img in tile_images:
    b = Button(tile_img, WIDTH + 20 + tile_col * 92, 20 + tile_row * 92, "tile")
    tile_btns.append(b)
    tile_col += 1
    if tile_col == 6:
        tile_row += 1
        tile_col = 0
for obj_img in object_images:
    b = Button(obj_img, WIDTH + 20 + tile_col * 92, 20 + tile_row * 92, "object")
    tile_btns.append(b)
    tile_col += 1
    if tile_col == 6:
        tile_row += 1
        tile_col = 0

COLS = 150
ROWS = HEIGHT//50
TILE_SIZE = 50

def draw_lines():
    for i in range(ROWS + 1):
        pygame.draw.line(screen, "darkgreen", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    
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
    draw_lines()
    for btn in tile_btns:
        btn.update(screen)


    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Maintain the frame rate
pygame.quit()  # Quit pygame


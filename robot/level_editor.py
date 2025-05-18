import pygame 
from button import Button
import pickle
pygame.init()  # Initialize pygame
import os
WIDTH = 800
HEIGHT = 600
SIDE_MARGIN = 600
LOWER_MARGIN = 100
FPS = 60
COLS = 150
ROWS = HEIGHT//50
TILE_SIZE = 50
current_tile = 0

level = 1






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
type_ = ''
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


world_data = []
for i in range(ROWS):
    temp = [-1] * COLS
    world_data.append(temp)
def draw_world():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] != -1:             
                    screen.blit(tile_btns[world_data[i][j]].image, (j * TILE_SIZE,i * TILE_SIZE))

def draw_lines():
    for i in range(ROWS + 1):
        pygame.draw.line(screen, "darkgreen", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    for i in range(COLS + 1):
        pygame.draw.line(screen, "darkgreen", (i * TILE_SIZE, 0), (i *TILE_SIZE, HEIGHT))

def save_level(level):
    with open(f"level{level}", "wb") as f:
        pickle.dump(world_data, f)
def load_level(level):
    with open(f"level{level}", "rb") as f:
         w = pickle.load(f)

    return w


screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))   
pygame.display.set_caption("Level Editor")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_level(level)
            if event.key == pygame.K_l:
                world_data = load_level(level)

    screen.fill("white")  
    draw_lines()

    mouse_pos = pygame.mouse.get_pos()
    c = mouse_pos[0]//TILE_SIZE
    r = mouse_pos[1]//TILE_SIZE
    
    pygame.draw.rect(screen, "lightblue", (WIDTH, 0, SIDE_MARGIN,HEIGHT + LOWER_MARGIN))  
    pygame.draw.rect(screen, "lightblue", (0, HEIGHT,WIDTH +  SIDE_MARGIN, HEIGHT)) 
    for i,btn in enumerate(tile_btns):
        x = btn.update(screen)
        if x[0]:
            current_tile =  i
            type_ = x[1]

    if pygame.mouse.get_pressed()[0] and mouse_pos[0] < WIDTH and mouse_pos[1] < HEIGHT:
        world_data[r][c] = current_tile

    pygame.draw.rect(screen, "red", tile_btns[current_tile].rect, 4)
    draw_world()
    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Maintain the frame rate
pygame.quit()  # Quit pygame


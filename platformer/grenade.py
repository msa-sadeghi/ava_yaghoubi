from pygame.sprite import Sprite
import pygame

class Grenade(Sprite):
    def __init__(self, x,y,group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(center=(x,y))
        self.direction = direction
        self.xspeed = 5
        self.yspeed = -10
        group.add(self)
        
    def update(self):
        dx = 0
        dy = 0
        dx += self.xspeed
        dy += self.yspeed
        self.yspeed += 1
        
        self.rect.x += dx
        self.rect.y += dy
from pygame.sprite import Sprite
import pygame

from explosion import Explosion

class Grenade(Sprite):
    def __init__(self, x,y,group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(center=(x,y))
        self.direction = direction
        self.xspeed = 5
        self.yspeed = -10
        group.add(self)
        self.timer = 100
        
    def update(self,group):
        dx = 0
        dy = 0
        dx += self.direction * self.xspeed
        dy += self.yspeed
        self.yspeed += 1
        if self.rect.bottom + dy >= 300:
            dy = 300 - self.rect.bottom
            dx = 0
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            Explosion(
                self.rect.centerx,
                self.rect.centery,
                group
            )    
        self.rect.x += dx
        self.rect.y += dy
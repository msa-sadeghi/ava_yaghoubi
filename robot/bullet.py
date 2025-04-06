from pygame.sprite import Sprite
import pygame   
class Bullet(Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.all_images = [
            pygame.image.load(f"./Objects/Bullet/Bullet_00{i}.png")
            for i in range(5)
        ]
        self.image = self.all_images[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = direction
        self.frame_index = 0
        self.last_animation_time = pygame.time.get_ticks()
        self.speed = 10

    def update(self):
        if pygame.time.get_ticks() - self.last_animation_time  >= 100:
            self.last_animation_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images):
                self.frame_index = 0
        self.rect.x += self.direction * self.speed
        self.image = self.all_images[self.frame_index]
        
        # Remove the bullet if it goes off screen
        if self.rect.x < 0 or self.rect.x > 800:
            self.kill()
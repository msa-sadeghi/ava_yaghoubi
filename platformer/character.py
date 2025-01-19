from pygame.sprite import Sprite
import pygame
import os
class Character(Sprite):
    def __init__(self, type_, x,y,ammo, grenades):
        super().__init__()
        self.type_ = type_
        self.ammo = ammo
        self.grenades = grenades
        self.alive = True
        self.health = 100
        self.max_health = 100
        self.all_images = {}
        self.animation_types = os.listdir(f"./assets/images/{type_}")
        for animation in self.animation_types:
            temp = []
            num_of_images = len(os.listdir(f"./assets/images/{type_}/{animation}"))
            for i in range(num_of_images):
                img = pygame.image.load(f"./assets/images/{type_}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 2, img_h * 2))
                temp.append(img)
            self.all_images[animation] = temp
        self.action = "Idle"
        self.image_number = 0
        self.image = self.all_images[self.action][self.image_number]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_image_change_time = pygame.time.get_ticks()
        self.flip = False
            
    def draw(self, screen):
        self.animation()
        img = self.all_images[self.action][self.image_number]
        img = pygame.transform.flip(img, self.flip, False)
        screen.blit(img, self.rect)
        
    def animation(self):
        
        if pygame.time.get_ticks() - self.last_image_change_time > 100:
            self.image_number += 1
            self.last_image_change_time = pygame.time.get_ticks()
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
                
    def move(self, moving_left, moving_right):
        dx = 0
        if moving_left:
            self.flip = True
            dx -= 5
        if moving_right:
            dx += 5
            self.flip = False
        
        
        self.rect.x += dx
        
            
        
    def change_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.image_number = 0
            self.last_image_change_time = pygame.time.get_ticks()        
        
        
        

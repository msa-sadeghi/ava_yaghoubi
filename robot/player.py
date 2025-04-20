from pygame.sprite import Sprite
import pygame
import os

from bullet import Bullet
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.animation_types = os.listdir("./png")
        self.all_images = {}
        for animation in self.animation_types:
            temp = []
            num_of_images = len(os.listdir(f"./png/{animation}"))
            for i in range(1, num_of_images):
                img = pygame.image.load(f"./png/{animation}/{animation}{i}.png")
                img = pygame.transform.scale_by(img, 0.4)
                temp.append(img)

            self.all_images[animation] = temp
        self.action = "Idle"
        self.frame_index = 0
        self.image = self.all_images[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_animation_time = pygame.time.get_ticks()
        self.flip = False
        self.moving = False
        self.direction = 1
        self.slide = False
        self.jump = False
        self.yspeed = 0
        self.shooting = False

    def draw(self, screen):
       
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        self.animation()

    def animation(self):
        self.image = self.all_images[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.last_animation_time >= 100:
            self.frame_index += 1
            self.last_animation_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.moving = True
            self.flip = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.moving = True
            self.flip = False
            dx += 5
        
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False
        if keys[pygame.K_DOWN]:
            self.slide = True
            dx += self.direction * 10
        if not keys[pygame.K_DOWN]:
            self.slide = False
        if keys[pygame.K_UP]:
            self.jump = True
            self.yspeed = -15
        if keys[pygame.K_SPACE]:
            self.shooting = True
        if not keys[pygame.K_SPACE]:
            self.shooting = False
        dy += self.yspeed
        self.yspeed += 1
            
        if self.rect.bottom + dy > 500:
            self.yspeed = 0
            dy = 500 - self.rect.bottom
            self.jump = False


        self.rect.x += dx
        self.rect.y += dy

    def change_animation(self, new_action):
        if self.action != new_action:
            self.action = new_action
            self.frame_index = 0

    def shoot(self, bullet_group):
        if self.shooting:
            bullet = Bullet(self.rect.centerx + self.direction * self.rect.size[0]//2 + (self.direction * 10) ,
                             self.rect.centery - 40, self.direction)
            bullet_group.add(bullet)
import pygame

class Button:
    def __init__(self, image, x,y,type):
       
        self.image = pygame.transform.scale_by(
            pygame.image.load(image), 0.2)
        self.rect = self.image.get_rect(
            topleft=(x,y))
        self.type = type

    def update(self, screen):
        screen.blit(self.image, self.rect)
        click = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                click = True

        return click, self.type
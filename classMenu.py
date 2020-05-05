import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((340, 120))
        self.image.fill((255, 255, 255))
        self.image.set_alpha(50)
        self.rect = self.image.get_rect()
        self.rect.center = pos
import pygame

class PlaceForTurel():
    def __init__(self):
        self.krest = pygame.image.load('krest.png')
        self.krest = pygame.transform.scale(self.krest, (100, 100))
        self.rect = self.krest.get_rect()
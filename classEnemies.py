import pygame, random

class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = pygame.image.load('enemysheet.png')

        self.image = self.images.subsurface((0, 0, 125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = 578
        self.speed = 1
        self.health = 1000


    def update(self):
        self.run()
        if self.health <= 0:
            self.kill()

    def run(self):
        self.rect.y += self.speed



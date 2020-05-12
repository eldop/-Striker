import pygame
from math import sqrt

class Bullet(pygame.sprite.Sprite):
    def __init__(self, startpos, targetpos, damage, speed = 5):
        pygame.sprite.Sprite.__init__(self)
        self.rad = 3
        self.color = (255, 255, 255)
        self.image = pygame.Surface((6, 6))
        self.rect = self.image.get_rect()
        self.rect.center = startpos

        self.damage = damage
        self.speed = speed
        self.speedcalculation(targetpos, startpos)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.check()

    def check(self):
        if self.rect.top < 0 or self.rect.bottom > 720 or self.rect.right > 1280 or self.rect.left < 0:
            self.kill()


    def speedcalculation(self, targetpos, startpos):
        dx = targetpos[0] - startpos[0]
        dy = targetpos[1] - startpos[1]
        c = sqrt(dx**2 + dy**2)
        k = c/self.speed
        self.speedx = dx/k
        self.speedy = dy/k

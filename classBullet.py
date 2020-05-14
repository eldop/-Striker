import pygame
from math import sqrt

class Bullet(pygame.sprite.Sprite):
    def __init__(self, startpos, targetpos, damage, speed, color = (0,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.rad = 3
        self.color = color
        self.image = pygame.Surface((6, 6))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = startpos
        self.x = self.rect.x
        self.y = self.rect.y
        self.damage = damage
        self.speed = speed
        self.speedcalculation(targetpos, startpos)

    def update(self):
        self.y += self.speedy
        self.x += self.speedx
        self.rect.y = self.y
        self.rect.x = self.x
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

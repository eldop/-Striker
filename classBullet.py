import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, startpos, targetpos):
        pygame.sprite.Sprite.__init__(self)
        self.rad = 3
        self.color = (255, 255, 255)
        self.image = pygame.Surface((6, 6))
        self.rect = self.image.get_rect()
        self.rect.center = startpos
        self.speedx = (targetpos[0] - startpos[0])//50
        self.speedy = (targetpos[1] - startpos[1])//50

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

    def check(self):
        if self.rect.top < 0 or self.rect.bottom > 720 or self.rect.right > 1280 or self.rect.left < 0:
            self.kill()
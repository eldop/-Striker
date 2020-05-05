import pygame, random, math

class Turel(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.listimage = [pygame.image.load('turel1.png'), pygame.image.load('turel2.png'), pygame.image.load('turel3.png')]
        self.normalimage = random.choice(self.listimage)
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255,255,255))
        self.normalrect = self.normalimage.get_rect()
        self.normalrect.centerx = ((pos[0] // 80) * 80) + 40
        self.normalrect.centery = ((pos[1] // 80) * 80) + 40
        self.angle = 0
        self.image = self.normalimage
        self.rect = self.normalrect

    def update(self):
       # self.angle += 1
        self.rotate()


    def rotate(self):
        mpos = pygame.mouse.get_pos()
        self.angle = 0
        self.image = pygame.transform.rotate(self.normalimage, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.normalrect.center




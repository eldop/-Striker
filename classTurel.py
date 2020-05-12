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
        mposx, mposy = pygame.mouse.get_pos()
        dx = mposx - self.normalrect.centerx
        dy = mposy - self.normalrect.centery
        rangel = math.atan2(-dy, dx)
        self.angle = math.degrees(rangel)
        #self.angle = 0
        self.image = pygame.transform.rotate(self.normalimage, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.normalrect.center


class BasicTurel(Turel):
    def __init__(self, pos):
        Turel.__init__(self, pos)
        self.normalimage = pygame.image.load('turel1.png')
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255, 255, 255))
        self.damage = 10
        self.bulletspeed = 10

class HeavyTurel(Turel):
    def __init__(self, pos):
        Turel.__init__(self, pos)
        self.normalimage = pygame.image.load('turel2.png')
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255,255,255))
        self.damage = 25
        self.bulletspeed = 3

class SpeedyTurel(Turel):
    def __init__(self, pos):
        Turel.__init__(self, pos)
        self.normalimage = pygame.image.load('turel3.png')
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255, 255, 255))
        self.damage = 5
        self.bulletspeed = 20




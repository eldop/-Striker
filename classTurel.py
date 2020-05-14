import pygame, random, math, classEnemies, classBullet

class Turel(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.listimage = [pygame.image.load('turel1.png'), pygame.image.load('turel2.png'), pygame.image.load('turel3.png'),  pygame.image.load('turel4.png')]
        self.normalimage = random.choice(self.listimage)
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255,255,255))
        self.normalrect = self.normalimage.get_rect()
        self.normalrect.centerx = ((pos[0] // 80) * 80) + 40
        self.normalrect.centery = ((pos[1] // 80) * 80) + 40
        self.angle = 0
        self.image = self.normalimage
        self.rect = self.normalrect
        self.bullets = pygame.sprite.Group()
        self.bulletspeed = 8374621
        self.damage = 413412


    def update(self, display):
       # self.angle += 1
        self.rotate()
        self.bullets.update()
        self.bullets.draw(display)


    def rotate(self):

        mposx, mposy = pygame.mouse.get_pos()
        dx = mposx - self.normalrect.centerx
        dy = mposy - self.normalrect.centery
        rangel = math.atan2(-dy, dx)
        self.angle = math.degrees(rangel)
        #self.angle = 0
        self.image = pygame.transform.rotate(self.normalimage, self.angle)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = self.normalrect.center

    def shoot(self, pos):
        b = classBullet.Bullet(self.rect.center, pos, self.damage, self.bulletspeed)
        self.bullets.add(b)




turel = [pygame.image.load('turel1.png'), pygame.image.load('turel2.png'), pygame.image.load('turel3.png'), pygame.image.load('turel4.png')]
class BasicTurel(Turel):
    def __init__(self, pos):
        Turel.__init__(self, pos)
        self.normalimage = turel[0]
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255, 255, 255))
        self.damage = 10
        self.bulletspeed = 10

class HeavyTurel(Turel):
    def __init__(self, pos):
        Turel.__init__(self, pos)
        self.normalimage = turel[1]
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255,255,255))
        self.damage = 25
        self.bulletspeed = 3


class SpeedyTurel(Turel):
    def __init__(self, pos):
        Turel.__init__(self, pos)
        self.normalimage = turel[2]
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255, 255, 255))
        self.damage = 5
        self.bulletspeed = 20


colors = {
    'red':(255, 0 ,0),
    'orange':(255,110,0),
    'yellow':(255,200,0),
    'green':(0, 255, 0),
    'lblue':(0, 215, 255),
    'blue':(0,0,255),
    'purple':(255, 0, 255)
}


class RainbowTurel(Turel):
    def __init__(self, pos):
        Turel.__init__(self, pos)
        self.normalimage = turel[3]
        self.normalimage = pygame.transform.scale(self.normalimage, (80, 80))
        self.normalimage.set_colorkey((255, 255, 255))
        self.damage = random.randint(5, 30)
        self.bulletspeed = random.randint(5, 30)

    def shoot(self, pos):
        color = random.choice(list(colors.values()))
        print(color)
        b = classBullet.Bullet(self.rect.center, pos, self.damage, self.bulletspeed, color)
        self.bullets.add(b)






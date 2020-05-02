import pygame, random
pygame.init()

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont('Algerian', 40)
        self.loadimages = pygame.image.load('enemysheet.png')
        self.color = GREEN
        self.loadimage = self.loadimages.subsurface((0, 0, 125, 125))
        self.rect = self.loadimage.get_rect()
        self.loadimage = pygame.transform.rotate(self.loadimage, -90)
        self.rect.x = -200
        self.rect.centery = 360
        self.speed = 1
        self.health = 1000
        self.texthealth = self.font.render(str(self.health), 1, self.color)
        self.image = self.loadimage.copy()
        self.image.blit(self.texthealth, (0,0))




    def update(self):
        self.run()

        if self.health <= 0:
            self.kill()

    def run(self):
        self.rect.x += self.speed

    def damage(self):
        self.health -= 5
        if self.health > 500:
            self.color = GREEN
        elif 250 < self.health < 500:
            self.color = BLUE
        else:
            self.color = RED
        self.image = self.loadimage.copy()
        self.texthealth = self.font.render(str(self.health), 1, self.color)
        self.image.blit(self.texthealth, (0, 0))



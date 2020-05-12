import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((320, 120))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        #self.image.set_alpha(50)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        ramka = pygame.image.load('ramka.png')
        ramka = pygame.transform.scale(ramka, (320, 120))
        turelimage1 = pygame.image.load('turel1.png')
        turelimage1= pygame.transform.scale(turelimage1, (80, 80))
        turelimage2 = pygame.image.load('turel2.png')
        turelimage2 = pygame.transform.scale(turelimage2, (80, 80))
        turelimage3 = pygame.image.load('turel3.png')
        turelimage3 = pygame.transform.scale(turelimage3, (80, 80))
        self.image.blit(ramka, (0,0))
        self.image.blit(turelimage1, (20, 20))
        self.image.blit(turelimage2, (120, 20))
        self.image.blit(turelimage3, (220, 20))

    def turelchoice(self, pos):
        mposx, mposy = pos
        rx = mposx - self.rect.x
        if 20<rx<120:
            return 1
        elif 120<rx<220:
            return 2
        elif 220<rx<320:
            return 3
        else:
            return 0
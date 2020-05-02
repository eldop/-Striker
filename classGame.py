import pygame, classTurel, classEnemies, classBullet
pygame.init()



class Game():
    def __init__(self):
        self.font = pygame.font.SysFont('Algerian', 40)

        self.background = pygame.image.load('background.jpg')

        self.FPS = 30
        self.clock = pygame.time.Clock()



        self.enemygroup = pygame.sprite.LayeredUpdates()
        self.turelgroup = pygame.sprite.LayeredUpdates()

        self.over = False
        self.display = pygame.display.set_mode((1280, 720))

        pygame.display.set_caption('-Striker')
        pygame.display.set_icon(pygame.image.load('icon.png'))

        self.bullets = pygame.sprite.Group()

        self.money = 500

    def update(self):
        self.clock.tick(self.FPS)
        self.display.fill((255, 180, 10))
        self.kvadratiki()
        self.turelgroup.update()
        self.enemygroup.update()
        self.bullets.update()
        self.turelgroup.draw(self.display)
        self.enemygroup.draw(self.display)

        self.bullets.draw(self.display)
        self.checkaim()
        self.textmoney = self.font.render(str(self.money), 1, (0,0,0))
        self.display.blit(self.textmoney, (0, 0))
        pygame.display.update()


    def spawnenemy(self):
        self.enemygroup.add(classEnemies.Enemies())



    def spawnturel(self, pos):
        if self.money >= 100:
            self.turelgroup.add(classTurel.Turel(pos))
            self.money -= 100

    def kvadratiki(self):
        for dx in range(0, 1280, 160):
            for dy in range(0, 720, 80):
                if dy % 160 != 0:
                    pygame.draw.rect(self.display, (255,190,0), (dx + 80, dy, 80, 80))
                else:
                    pygame.draw.rect(self.display, (255,190,0), (dx, dy, 80, 80))

    def shoot(self, pos):
        self.bullets.add(classBullet.Bullet(self.rect.center, pos))

    def shootall(self, pos):
        for turel in self.turelgroup:
            b = classBullet.Bullet(turel.rect.center, pos)
            self.bullets.add(b)

    def checkaim(self):

        for enemy in pygame.sprite.groupcollide(self.enemygroup, self.bullets, False, True):
            enemy.damage()
            self.money += 5




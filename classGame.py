import pygame, classTurel, classEnemies, classBullet, classMenu
pygame.init()



class Game():
    def __init__(self):
        self.font = pygame.font.SysFont('Algerian', 40)

        self.background = pygame.image.load('background.jpg')

        self.FPS = 30
        self.clock = pygame.time.Clock()



        self.enemygroup = pygame.sprite.LayeredUpdates()
        self.turelgroup = pygame.sprite.LayeredUpdates()
        self.menugroup = pygame.sprite.LayeredUpdates()

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
        self.menugroup.update()
        self.bullets.update()
        self.turelgroup.draw(self.display)
        self.enemygroup.draw(self.display)
        self.menugroup.draw(self.display)

        self.bullets.draw(self.display)
        self.checkaim()
        self.textmoney = self.font.render(str(self.money), 1, (0,0,0))
        self.display.blit(self.textmoney, (0, 0))
        pygame.display.update()



    def spawnenemy(self):
        self.enemygroup.add(classEnemies.Enemies())



    def spawnturel(self, pos, numberofturel):
        if self.money >= 100:
            if len(self.turelgroup.get_sprites_at(pos)) == 0:
                if numberofturel == 1:
                    self.turelgroup.add(classTurel.BasicTurel(pos))
                if numberofturel == 2:
                    self.turelgroup.add(classTurel.HeavyTurel(pos))
                if numberofturel == 3:
                    self.turelgroup.add(classTurel.SpeedyTurel(pos))
                self.money -= 100

    def kvadratiki(self):
        for dx in range(0, 1280, 160):
            for dy in range(0, 720, 80):
                if dy % 160 != 0:
                    pygame.draw.rect(self.display, (255,190,0), (dx + 80, dy, 80, 80))
                else:
                    pygame.draw.rect(self.display, (255,190,0), (dx, dy, 80, 80))



    def shootall(self, pos):
        for turel in self.turelgroup:
            b = classBullet.Bullet(turel.rect.center, pos, turel.damage, turel.bulletspeed)
            self.bullets.add(b)

    def checkaim(self):
        collision = pygame.sprite.groupcollide(self.enemygroup, self.bullets, False, True)

        for enemy in collision:
            for bullet in collision[enemy]:
                enemy.damage(bullet.damage)
            #damage = collision[enemy].damage


            self.money += 1

    def showmenu(self, pos):
        #не попали в меню
        if len(self.menugroup.get_sprites_at(pos)) == 0:
            for i in self.menugroup.sprites():
                i.kill()


            self.menu = classMenu.Menu(pos)
            self.menugroup.add(self.menu)

        #попали в меню
        else:
            numberofturel = self.menu.turelchoice(pos)


            self.spawnturel(self.menu.rect.center, numberofturel)
            for i in self.menugroup.sprites():
                i.kill()




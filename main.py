from pygame import event, mixer, time
from pygame.locals import *
import classGame

game = classGame.Game()


time.set_timer(USEREVENT, 4444)

while not game.over:
    for e in event.get():
        if e.type == QUIT:
            game.over = True
        if e.type == USEREVENT:
            game.spawnenemy()
        if e.type == MOUSEBUTTONUP:
            if e.button == 3:
                #game.spawnturel(e.pos)
                game.showmenu(e.pos)
            if e.button == 1:
                game.shootall(e.pos)
    game.update()
import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 10
WINDOW_SIZE = (700, 700)
BACKGROUND = (190, 90, 30)
screen = pg.display.set_mode(WINDOW_SIZE)

screen.fill(BACKGROUND)
pg.display.update()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    clock.tick(FPS)
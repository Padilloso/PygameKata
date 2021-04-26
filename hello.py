import pygame as pg

pg.init()

pantalla = pg.display.set_mode((600,400))
pg.display.set_caption("Hola")

game_over = False

while  not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameOver = True

    pantalla.fill((0,255,0))

    pg.display.flip()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close()
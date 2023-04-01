import  pygame
from ball import *
from gun import *
from ellips import *
from rectangl import *
from colors import BLACK
from pygame.draw import *
from random import randint

pygame.init()
pygame.font.init()

score  = 0
FPS = 60
size = Vector(1200, 900)
screen = pygame.display.set_mode(size.get())
gun = Gun(screen)
units = [Ball(screen) for i in range(5)] + [Rectangl(screen) for i in range(7)] + [Ellipse(screen) for i in range(2)]
units.append(gun)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        welcome_text = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 30), 'Счет: '+ str(score), True, (200, 0, 0))
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEMOTION:
            gun.setMouse(*event.pos)
            # gun.setMouse(626,577)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cor = event.pos
            for i,unit in enumerate(units):
                score += unit.check(*cor)
                if unit.is_dead():
                    units.pop(i)
                    
    for unit in units:
        unit.draw()
        unit.move()

    screen.blit(welcome_text, (1000, 800))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()


"""
# SCROLL DOWN FOR KIVGAME EXAMPLE
# ORIGINAL BY INVENTWITHPYTHON: CHAPTER 2
# http://inventwithpython.com/pygame/chapters/
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
"""

from kivgame.pygame import pygame as pg
from kivgame.locals import *
pygame = pg.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), RESIZABLE, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('img/cat.png')

# keep changing variables in an object
# to prevent unresolved references
class Cat(object):
    x = 10
    y = 10
    direction = 'right'

cat = Cat()

def loop():
    DISPLAYSURF.fill(WHITE)

    if cat.direction == 'right':
        cat.x += 5
        if cat.x == 280:
            cat.direction = 'down'
    elif cat.direction == 'down':
        cat.y += 5
        if cat.y == 220:
            cat.direction = 'left'
    elif cat.direction == 'left':
        cat.x -= 5
        if cat.x == 10:
            cat.direction = 'up'
    elif cat.direction == 'up':
        cat.y -= 5
        if cat.y == 10:
            cat.direction = 'right'

    DISPLAYSURF.blit(catImg, (cat.x, cat.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # this 2 lines are not mandatory
    # main loop is default 32 FPS but clock.tick can alter it
    # display.update is just for backwards compatibility
    fpsClock.tick(FPS)
    pygame.display.update()

def main():
    pygame.set_loop(loop)
    pygame.run()

if __name__ == "__main__":
    main()
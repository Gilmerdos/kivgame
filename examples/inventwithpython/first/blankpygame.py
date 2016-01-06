"""
# SCROLL DOWN FOR KIVGAME EXAMPLE
# ORIGINAL BY INVENTWITHPYTHON: CHAPTER 2
# http://inventwithpython.com/pygame/chapters/
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Pygame World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

"""
from kivgame.pygame import pygame as pg
from kivgame.locals import *
pygame = pg.init()

DISPLAYSURF = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Hello Pygame World!', 'icon.png')

def loop():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

def main():
    pygame.set_loop(loop)
    pygame.run()

if __name__ == "__main__":
    main()
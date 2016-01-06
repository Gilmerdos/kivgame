
#Pygame syntax for Kivy game development

just cause it would be nice to write pygame code and make advantage of Kivy's wonderful UI widgets!
[Visit Kivy!](https://www.kivy.org)

#Why ?

I want to use Python for making Android games, pgs4a is a good option but there aren't native UI widgets in Pygame
Also Kivy's widgets can resize and adapt to the user screen, which is good

Unity was also an option but they don't have a fixed screen option, this can be implemented in Kivy
On Android platforms it will autoscale your game to fit fullscreen on the device ( currently working for a basic example :) )

Also e.g. screen.blit(img, (x, y)) autoscales the position if the screen is stretched

#Note:
project is in very early stages, I'm only refactoring the code ( cleaning up ) when i'm satisfied with the project

#Basic Kivgame template

```python
from kivgame.pygame import pygame as pg
from kivgame.locals import *
pygame = pg.init()

screen = pygame.display.set_mode((640, 480), flags) # Flags could be: FULLSCREEN | NO_FRAME | RESIZABLE
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
```


#Some examples so far

##catanimation.py (resizable version)
![Alt text](examples/inventwithpython/first/showcase/catanimation_resizable.gif?raw=true "catanimation.py")

##drawing.py
![Alt text](examples/inventwithpython/first/showcase/drawing.png?raw=true "drawing.py")

##blankpygame.py
![Alt text](examples/inventwithpython/first/showcase/blankpygame.png?raw=true "blankpygame.py")


#Pygame syntax for Kivy game development

just cause it would be nice to write pygame code and make advantage of Kivy's wonderful UI widgets!
[Visit Kivy!](https://www.kivy.org)

#Basic Kivgame template

```python
from kivgame.pygame import pygame as pg
from kivgame.locals import *
pygame = pg.init()

screen = pygame.display.set_mode((640, 480))
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

##blankpygame.py
![Alt text](examples/inventwithpython/first/showcase/blankpygame.png?raw=true "blankpygame.py")

##drawing.py
![Alt text](examples/inventwithpython/first/showcase/drawing.png?raw=true "drawing.py")
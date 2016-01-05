#Pygame imports
from sys import exit
from .surface import Surface
from .display import Display
from .image import Image
from .event import Event

class Pygame(object):
    def __init__(self):
        self.display = Display()
        self.image = Image()
        self.event = Event()

    def quit(self):
        exit()

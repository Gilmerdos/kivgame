from sys import exit
from .display import Display
from .image import Image
from .event import Event
from .draw import Draw
from .time import Time
from .pixelarray import PixelArray

class Pygame(object):
    def __init__(self):
        self.display = Display()
        self.image = Image()
        self.event = Event()
        self.draw = Draw()
        self.time = Time()
        self.PixelArray = PixelArray

    def quit(self):
        exit()

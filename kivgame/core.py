#Pygame imports
from .surface import Surface
from .display import Display
from .image import Image

class Pygame(object):
    def __init__(self):
        self.display = Display()
        self.image = Image()
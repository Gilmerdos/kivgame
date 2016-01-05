from kivy.uix.image import Image as KivyImage
from .surface import Surface

class Image(object):
    def __init__(self, window=None):
        self.window = None

    def load(self, file=None):
        return Surface(KivyImage(source=file).texture)
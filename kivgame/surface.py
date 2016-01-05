from .rect import Rect

class Surface(object):
    def __init__(self, texture=None):
        self.width = texture.width
        self.height = texture.height
        self.texture = texture

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_rect(self):
        return Rect(self.texture)
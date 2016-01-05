
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.base import EventLoop
from .locals import *

class Dummy(object):
    pass

class Display(object):
    def __init__(self, window=None):
        self.width = -1
        self.height = -1
        self.window = None
        self.app = None
        self.size = (640, 480)
        self.resizable = False

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_mode(self, size=(640,480), flags=0, depth=0):
        if OPENGL <= flags:
            flags -= OPENGL

        if NOFRAME <= flags:
            flags -= NOFRAME
            Window.borderless = "1"

        if RESIZABLE <= flags:
            flags -= RESIZABLE
            self.resizable = True

        if HWSURFACE <= flags:
            flags -= HWSURFACE

        if DOUBLEBUF <= flags:
            flags -= DOUBLEBUF

        if FULLSCREEN <= flags:
            flags -= FULLSCREEN
            Window.fullscreen = True




        Window.size = size
        self.size = size
        self.width, self.height = size
        self.width = float(self.width)
        self.height = float(self.height)
        canvas = Dummy()
        canvas.blit = self.blit
        canvas.get_width = self.get_width
        canvas.get_height = self.get_height
        return canvas

    def set_caption(self, title, icontitle=None):
        self.app.title = title
        if icontitle != None:
            self.app.icon = icontitle

    def blit(self, source, dest, area=None, special_flags=0):
        try:
            dest = (dest[0], self.height - dest[1] - source.height)
        except:
            dest = (dest.x, self.height - dest.y - source.height)

        ratio = Window.width / self.width, Window.height / self.height
        size = source.texture.width * ratio[0], source.texture.height * ratio[1]
        dest = [dest[0] * ratio[0], dest[1] * ratio[1]]
        with self.window.canvas:
            Rectangle(texture=source.texture, pos=dest, size=size)

    def flip(self):
        return None

    def update(self):
        return None
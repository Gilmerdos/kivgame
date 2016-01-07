
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.base import EventLoop
from .locals import *

try:
    import android
except:
    android = False

class DummyDisplay(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

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

        self.size = size
        self.width, self.height = size
        if not android: Window.size = size
        self.width = float(self.width)
        self.height = float(self.height)
        canvas = DummyDisplay(self.width, self.height)
        canvas.blit = self.blit
        canvas.fill = self.fill
        canvas.clear = self.clear
        canvas.get_width = self.get_width
        canvas.get_height = self.get_height
        return canvas

    def set_caption(self, title, icontitle=None):
        self.app.title = title
        if icontitle != None:
            self.app.icon = icontitle

    def clear(self):
        self.window.canvas.clear() #to avoid memory leaks

    def fill(self, color, rect=None, special_flags=0):
        R = color[0] / 255.0
        G = color[1] / 255.0
        B = color[2] / 255.0
        self.window.canvas.clear() #to avoid memory leaks
        with self.window.canvas:
            Color(R, G, B)
            Rectangle(size=(Window.width, Window.height))

    def blit(self, source, dest=(0, 0), area=None, special_flags=0):
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
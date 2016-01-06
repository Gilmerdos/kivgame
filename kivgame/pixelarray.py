from kivy.graphics import Point
from kivy.graphics import Color

class PixelArray(object):
    def __init__(self, Surface):
        self.height = Surface.height

    def __setitem__(self, point, value):
        R = value[0] / 255.0
        G = value[1] / 255.0
        B = value[2] / 255.0
        with self.window.canvas:
            Color(R, G, B)
            Point(points=(point[0], self.height - point[1]))

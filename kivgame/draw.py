from kivy.graphics import Line
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

class Draw(object):
    def __init__(self):
        self.window = None

    def RGBify(self, color):
        R = color[0] / 255.0
        G = color[1] / 255.0
        B = color[2] / 255.0
        return R, G, B

    def polygon(self, Surface, color, pointlist, width=0):
        # TODO: implement method to fill the polygon (MESH?)
        R, G, B = self.RGBify(color)
        points = ([float(c) if i == 0  else Surface.height - float(c)
                   for coords in pointlist for i, c in enumerate(coords)])

        with self.window.canvas:
            Color(R, G, B)
            Line(points=points, width=width)

    def line(self, Surface, color, start_pos, end_pos, width=1):
        R, G, B = self.RGBify(color)
        pointlist = (start_pos, end_pos)
        points = ([float(c) if i == 0  else Surface.height - float(c)
                   for coords in pointlist for i, c in enumerate(coords)])

        with self.window.canvas:
            Color(R, G, B)
            Line(points=points, width=width)

    def circle(self, Surface, color, pos, radius, width=0):
        # TODO: implement method to fill the circle (MESH?)
        R, G, B = self.RGBify(color)
        with self.window.canvas:
            Color(R, G, B)
            Line(circle=(pos[0], Surface.height - pos[1], radius))

    def ellipse(self, Surface, color, rect, width=0):
        # TODO: implement method to fill the ellipse (MESH?)
        R, G, B = self.RGBify(color)
        with self.window.canvas:
            Color(R, G, B)
            Line(ellipse=(rect[0], Surface.height - rect[1] - rect[3], rect[2], rect[3]))

    def rect(self, Surface, color, rect, width=0):
        R, G, B = self.RGBify(color)
        if width == 0:
            with self.window.canvas:
                Color(R, G, B)
                Rectangle(pos=(rect[0], Surface.height - rect[1] - rect[3]),
                          size=(rect[2], rect[3]))
        else:
            with self.window.canvas:
                Color(R, G, B)
                # TOP LEFT > BOTTOM LEFT

                Line(points=(rect[0], Surface.height - rect[1],
                             rect[0], Surface.height - rect[1] - rect[3]),
                     width=width)

                # BOTTOM LEFT > BOTTOM RIGHT
                Line(points=(rect[0], Surface.height - rect[1] - rect[3],
                             rect[0] + rect[2], Surface.height - rect[1] - rect[3]),
                     width=width)

                # BOTTOM RIGHT > TOP RIGHT
                Line(points=(rect[0] + rect[2], Surface.height - rect[1] - rect[3],
                             rect[0] + rect[2], Surface.height - rect[1]),
                     width=width)

                # TOP RIGHT > TOP LEFT
                Line(points=(rect[0] + rect[2], Surface.height - rect[1],
                             rect[0], Surface.height - rect[1]),
                     width=width)

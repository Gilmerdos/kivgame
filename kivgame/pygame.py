import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from .core import Pygame

class KivGameApp(App):
    def build(self):
        Clock.schedule_interval(self.pygame.wrapper_loop, 0.032)
        return self.pygame.window

def init():
    app = KivGameApp()
    app.pygame = pygame
    app.pygame.window = FloatLayout()

    app.display = app.pygame.display
    app.display.window = app.pygame.window

    app.image = app.pygame.image
    app.image.window = app.pygame.window

    app.set_loop = app.pygame.set_loop
    return app

def wrapper_loop(*args):
    pygame.window.canvas.clear()
    pygame.loop()

def set_loop(loop):
    pygame.loop = loop
    pygame.wrapper_loop = wrapper_loop

pygame = Pygame()
pygame.set_loop = set_loop
pygame.init = init



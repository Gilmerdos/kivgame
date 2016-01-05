import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from .core import Pygame

class Canvas(FloatLayout):
    """ http://stackoverflow.com/a/17296090 """
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        Window.bind(on_resize=self.resize)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pygame.event.add_event(keycode)
        return True

    def resize(self, *args):
        if not self.pygame.display.resizable and Window.size != self.pygame.display.size:
            Window.size = self.pygame.display.size

class KivGameApp(App):
    def build(self):
        Clock.schedule_interval(self.pygame.wrapper_loop, 0.032)
        return self.pygame.window

def init():
    app = KivGameApp()
    app.pygame = pygame
    app.pygame.window = Canvas()
    app.pygame.window.pygame = pygame

    app.quit = app.pygame.quit
    app.event = app.pygame.event

    app.display = app.pygame.display
    app.display.app = app

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



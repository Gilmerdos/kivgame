import kivy
from kivy.app import App
from kivy.clock import Clock as KivyClock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from .core import Pygame
from .locals import *
try:
    import android
except:
    android = False

class Canvas(FloatLayout):
    """ http://stackoverflow.com/a/17296090 """
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)
        if not android:
            self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
            self._keyboard.bind(on_key_down=self._on_keyboard_down)
        Window.bind(on_resize=self.resize)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pygame.event.add_mouse_event(touch, MOUSEBUTTONDOWN)
            return True

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.pygame.event.add_mouse_event(touch, MOUSEMOTION)
            return True

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.pygame.event.add_mouse_event(touch, MOUSEBUTTONUP)
            return True

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pygame.event.add_event(keycode)
        return True

    def resize(self, *args):
        if not android:
            if not self.pygame.display.resizable and Window.size != self.pygame.display.size:
                Window.size = self.pygame.display.size

class KivGameApp(App):
    def build(self):
        self.clock = self.pygame.time.Clock()
        self.clock_fps = 0.03125
        self.clock_interval = KivyClock.schedule_interval(self.pygame.wrapper_loop, self.clock_fps)
        return self.pygame.window

def init():
    app = KivGameApp()
    app.pygame = pygame
    app.pygame.window = Canvas()
    app.pygame.window.pygame = pygame

    app.quit = app.pygame.quit
    app.event = app.pygame.event

    app.display = app.pygame.display
    app.display.window = app.pygame.window
    app.display.app = app

    app.image = app.pygame.image
    app.image.window = app.pygame.window

    app.draw = app.pygame.draw
    app.draw.window = app.pygame.window

    app.time = app.pygame.time
    app.time.Clock.app = app
    app.time.window = app.pygame.window

    app.Rect = app.pygame.Rect
    app.Rect.window = app.pygame.window

    app.PixelArray = app.pygame.PixelArray
    app.PixelArray.window = app.pygame.window

    app.set_loop = app.pygame.set_loop
    return app

def wrapper_loop(*args):
    #pygame.window.canvas.clear()
    pygame.loop()

def set_loop(loop):
    pygame.loop = loop
    pygame.wrapper_loop = wrapper_loop
    pygame

pygame = Pygame()
pygame.set_loop = set_loop
pygame.init = init



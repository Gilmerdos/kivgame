from kivy.core.window import Window
from .locals import *

class DummyEvent(object):
    def __init__(self, event):
        self.type = True
        self.ascii = event[0]
        self.char = event[0]
        self.key =  event[1]

        if self.key == "escape":
            self.type = QUIT

class DummyMouseEvent(object):
    def __init__(self, event, type):
        self.type = type
        self.pos = event.pos[0], Window.height - event.pos[1]
        self.spos = event.spos[0], 1.0 - event.spos[1]
        self.char = ''
        self.key = ''

class Event(object):
    def __init__(self):
        self.events = []

    def add_event(self, event):
        e = DummyEvent(event)
        self.events.append(e)

    def add_mouse_event(self, event, type):
        e = DummyMouseEvent(event, type)
        self.events.append(e)

    def get(self):
        for event in self.events:
            yield event
        self.events = []
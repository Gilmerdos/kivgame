from .locals import *

class DummyEvent(object):
    def __init__(self, event):
        self.type = "KEY_DOWN"
        self.char =  event[1]
        self.ascii = event[0]

        if self.char == "escape":
            self.type = QUIT


class Event(object):
    def __init__(self):
        self.events = []

    def add_event(self, event):
        e = DummyEvent(event)
        self.events.append(e)

    def get(self):
        for event in self.events:
            yield event
        self.events = []
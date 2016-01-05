from .locals import *

class DummyEvent(object):
    def __init__(self, event):
        self.type = "KEY_DOWN"
        self.char =  event[1]
        self.ascii = event[0]

    def __repr__(self):
        if self.char == "escape":
            self.type = QUIT

        return str({
            "type" : self.type,
            "char" : self.char,
            "ascii" : self.ascii
        })


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
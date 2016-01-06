import time
from kivy.clock import Clock as KivyClock

class Time(object):
    def __init__(self):
        self.Clock = Clock
        self.Clock.app = None

    def wait(self, milliseconds):
        """Don't use this!"""
        seconds = milliseconds / 1000.0
        time.sleep(seconds)

class Clock(object):
    def tick(self, framerate):
        try:
            if self.app.clock_fps != 1.0 / float(framerate):
                KivyClock.unschedule(self.app.clock_interval)
                self.app.clock_fps = 1.0 / float(framerate)
                self.app.clock_interval = KivyClock.schedule_interval(self.app.pygame.wrapper_loop, self.app.clock_fps)
        except:
            pass

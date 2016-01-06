from kivy.clock import Clock as KivyClock

class Time(object):
    def __init__(self):
        self.Clock = Clock
        self.Clock.app = None

class Clock(object):
    def tick(self, framerate):
        if self.app.clock_fps != 1.0 / float(framerate):
            KivyClock.unschedule(self.app.clock_interval)
            self.app.clock_fps = 1.0 / float(framerate)
            self.app.clock_interval = KivyClock.schedule_interval(self.app.pygame.wrapper_loop, self.app.clock_fps)


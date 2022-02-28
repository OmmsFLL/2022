from pybot.timed_loop import timed_loop


class Environment():
    def __init__(self, frequency):
        self.queue = []
    
    def run(self, frequency=10):
        for frame in timed_loop(frequency):
            if self.queue:
                try:
                    next(self.queue[0])
                except StopIteration:
                    del self.queue[0]
            else:
                break

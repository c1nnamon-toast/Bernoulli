import time

class Calculate:
    def __init__(self, start):
        self.start = start;
        time.sleep(1);
    
    def time(self, end):
        print("{0:.3f}" .format(end - self.start));

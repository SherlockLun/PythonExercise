import threading
import time

class Countdown:
    def __init__(self, seconds):
        self.seconds = seconds
        self.thread = threading.Thread(target=self.run)
        self.running = False

    def run(self):
        self.running = True
        while self.seconds > 0 and self.running:
            print(f" Time left: {self.seconds} seconds")
            time.sleep(1)
            self.seconds -= 1
        if self.running:
            self._beep()

    def _beep(self):
        print("Beep")

    def start(self):
        self.thread.start()

    def stop(self):
        self.running = False
        print("Countdown stopped.")
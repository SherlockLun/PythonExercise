import threading
import sys

class InputListener(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.running = True

    def run(self):
        while self.running:
            key = input("> ").strip().lower()
            if key == 'q':
                print("Stopping Input Listener...")
                sys.exit(0)
            elif key == 't':
                print("Ticking...")
            elif key == 'h':
                print("Help: Press 'q' to stop, 't' to tick, 'h' for help.")
            else:
                print(f" Unknown command: {key}. Press 'h' for help.")
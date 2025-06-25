import tkinter as tk
import time
from threading import Thread
from .countdown import Countdown

class CountdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Countdown")

        self.label = tk.Label(master, text="Seconds")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_countdown)
        self.start_button.pack()

        self.output = tk.Label(master, text="")
        self.output.pack()

    def start_countdown(self):
        try:
            seconds = int(self.entry.get())
            if seconds < 0:
                raise ValueError
        except ValueError:
            self.output.config(text="Enter non-negative integer")
            return
        
        Thread(target=self.run_countdown, args=(seconds,), daemon=True).start()

    def run_countdown(self, seconds):
        while seconds > 0:
            self.output.config(text=f"Time left: {seconds} seconds")
            time.sleep(1)
            seconds -= 1
        self.output.config(text="Beep")
import sys
from countdown import Countdown
from input_listener import InputListener

def parse_args():
    if len(sys.argv) != 2:
        print("Usage: python main.py <seconds>")
        sys.exit(1)
    try:
        seconds = int(sys.argv[1])
        if seconds < 0:
            raise ValueError("Seconds must be a non-negative integer.")
        return seconds
    except ValueError:
        print("Invalid input. Please enter a non-negative integer for seconds.")
        sys.exit(1)

if __name__ == "__main__":
    listener = InputListener()
    listener.start()
    
    seconds = parse_args()
    cd = Countdown(seconds)
    cd.start()
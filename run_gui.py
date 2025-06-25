from tkinter import Tk
from countdown.gui import CountdownApp

if __name__ == "__main__":
    root = Tk()
    app = CountdownApp(root)
    root.mainloop()
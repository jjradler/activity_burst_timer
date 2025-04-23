# activity_burst_timer.py
import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk


class ActivityBurstTimerApp(tk.Tk):
    """
    .. class:: ActivityBurstTimerApp
    .. desc:: Subclasses tk.Tk to create a small application window.
        This is the main high-level application.
    """
    def __init__(self):
        tk.Tk.__init__(self)
        # Offboard these into a different object class.
        seconds = 30
        self.max_time = seconds
        self.title("Activity Burst Timer v0.0.1")

        self.style = ttk.Style()
        self.style.theme_use('default')
        # how do I change this to match the system theme? 
        self.style.configure("black.Horizontal.TProgressbar", background='red')

        self.bar = Progressbar(self, length=220, style='black.Horizontal.TProgressbar')
        self.bar['value'] = 100
        self.bar.pack()

        self.label = tk.Label(self, text="", width=10)
        self.label.pack()

        # enclose this in a function that can handle the work timing portion
        self.remaining = 0
        self.countdown(seconds)

    # This should go into a timing module
    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            # This should go into an action method
            self.label.configure(text="Stop working!")
            self.bar['value'] = 0
            # TODO: Add a button to start break or restart the timer.
        else:
            # this should also go into an action function
            self.label.configure(text=f"{self.remaining}")
            if self.remaining > 0:
                self.bar['value'] = 100 * (self.remaining / self.max_time)
            self.remaining = self.remaining - 1
            # TODO: Change the 1000 to a variable
            self.after(1000, self.countdown)


if __name__ == "__main__":
    app = ActivityBurstTimerApp()
    app.mainloop()

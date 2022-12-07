# How can I make a drag and drop text gui using tkinter?

# I've been making a simple gui in python, and have been able to use grid to control the layout of components. However, I'd like to make a "textbox" component that I can drag and drop text to, like you'd find in a word processing program. How can I make a component like this in Tkinter? I've tried some things based on this SO post, but it's not helping. Here's what I have:
# import tkinter as tk

# class App(tk.Tk):

    # def __init__(self):
        # tk.Tk.__init__(self)

        # self.title("Mandelbrot set")

        # self.m1 = tk.StringVar()
        # self.m1.set("Click to start...")
        # self.m2 = tk.StringVar()
        # self.m2.set("Please wait...")

        # self.textbox = tk.Entry(self, textvariable=self.m1)
        # self.textbox.grid(row=0, column=0, columnspan=2, rowspan=2, sticky=tk.W+tk.E)

        # self.m3 = tk.StringVar()
        # self.m3.set("Please enter...")

        # self.textbox2 = tk.Entry(self, textvariable=self.m2)
        # self.textbox2.grid(row=1, column=0, sticky=tk.W+tk.E)

        # self.b = tk.Button(self, text="Go", command=self.start)
        # self.b.grid(row=1, column=2, sticky=tk.W+tk.E)

        # self.textbox.bind("<Button-1>", self.textboxClicked)

        # self.textbox2.bind("<Button-1>", self.textboxClicked)

    # def textboxClicked(self, event):
        # self.textbox.config(state=tk.DISABLED)
        # self.textbox2.config(state=tk.DISABLED)
        # self.textboxClicked.configure(text='')

    # def start(self):

        # self.textbox.config(state=tk.NORMAL)
        # self.textbox.bind("<ButtonRelease-1>", self.textboxClicked)

        # self.textbox.insert(0, self.m1.get())
        # self.textbox2.insert(0, self.m2.get())

        # self.textbox.config(state=tk.DISABLED)
        # self.textbox2.config(state=tk.DISABLED)

# if __name__ == "__main__":
    # App().mainloop()

# A:

# You can use .grid() to do this and you can configure the button to be draggable as seen in this question.
# Here is a working example of your original code:
import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Mandelbrot set")

        self.m1 = tk.StringVar()
        self.m1.set("Click to start...")
        self.m2 = tk.StringVar()
        self.m2.set("Please wait...")

        self.textbox = tk.Entry(self, textvariable=self.m1)
        self.textbox.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="we")

        self.m3 = tk.StringVar()
        self.m3.set("Please enter...")

        self.textbox2 = tk.Entry(self, textvariable=self.m2)
        self.textbox2.grid(row=1, column=0, sticky="we")

        self.b = tk.Button(self, text="Go", command=self.start)
        self.b.grid(row=1, column=2, sticky="we")

        self.textbox.grid_remove()
        self.textbox2.grid_remove()
        self.b.grid_remove()

        self.textbox.bind("<Button-1>", self.textboxClicked)
        self.textbox2.bind("<Button-1>", self.textboxClicked)

        self.b.bind("<ButtonRelease-1>", self.bButtonPressed)

    def textboxClicked(self, event):
        self.textbox.config(state=tk.DISABLED)
        self.textbox.bind("<ButtonRelease-1>", self.textboxClicked)
        self.textboxClicked.configure(text='')

    def bButtonPressed(self, event):
        self.textbox.config(state=tk.NORMAL)
        self.textbox.grid(row=0, column=0, sticky="we")
        self.textbox2.config(state=tk.NORMAL)
        self.textbox2.grid(row=1, column=0, sticky="we")

    def start(self):

        self.textbox.config(state=tk.DISABLED)
        self.textbox.bind("<ButtonRelease-1>", self.textboxClicked)
        self.textbox.insert(0, self.m1.get())
        self.textbox2.insert(0, self.m2.get())

        self.textbox.config(state=tk.DISABLED)
        self.textbox2.config(state=tk.DISABLED)

if __name__ == "__main__":
    App().mainloop()
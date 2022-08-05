from tkinter import *
from converter import runConvert
from tools import getlog


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title('URL to PDF (cagatayuresin)')
        self.window.resizable(False, False)
        self.window.iconbitmap('logo.ico')
        self.lbl = Label(self.window, text="URL: ")
        self.url = StringVar()
        self.txtfld = Entry(self.window, textvariable=self.url, justify='center', width=50)
        self.txtfld.bind('<Return>', lambda e: self.run())
        self.btn = Button(self.window, text='CONVERT', command=self.run)
        self.situation, self.color = getlog()
        self.situation_log = Label(self.window, text=self.situation, fg=self.color, font=('Helvetica', 7))

        self.loop()

    def loop(self):
        self.lbl.grid(row=0, column=0)
        self.txtfld.grid(row=0, column=1)
        self.txtfld.focus_set()

        self.btn.grid(row=1, column=0)
        self.situation_log.grid(row=1, column=1)
        self.window.mainloop()

    def run(self):
        runConvert(self.url.get())
        log, color = getlog()
        self.situation_log.config(text=log, fg=color)

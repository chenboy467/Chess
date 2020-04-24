from tkinter import *
import Chess
import functools
import math


class Launcher:
    def __init__(self, window):
        self.window = window
        self.window.title('Launcher')
        self.window.geometry('450x250')
        self.window.resizable(False, False)

        self.title = Label(window, text='Chess', font='Arial 48 bold')
        self.title.grid(row=0, columnspan=4, pady=10)

        '''self.easy_button = Button(window, text='EASY', font='Arial 18 bold',
                                  command=functools.partial(self.start, 10, 10), width=8)
        self.easy_button.grid(row=2, column=0, columnspan=1, padx=10, pady=3)'''

        self.start_button = Button(window, text='START', font='Arial 18 bold',
                                   command=functools.partial(self.start, 15, 15), width=8)
        self.start_button.grid(row=2, column=1, columnspan=1, padx=10, pady=3)

        '''self.hard_button = Button(window, text='HARD', font='Arial 18 bold',
                                  command=functools.partial(self.start, 20, 20), width=8)
        self.hard_button.grid(row=2, column=2, columnspan=1, padx=10, pady=3)

        self.custom_frame = Frame(window)
        self.custom_frame.grid(row=3, column=2, columnspan=1, pady=10)
        Label(self.custom_frame, text='Rows:      ', font='Arial 12').grid(
            row=0, column=0, columnspan=1)
        self.rows_select = Spinbox(self.custom_frame, from_=4, to=50, width=3)
        self.rows_select.grid(row=0, column=1, columnspan=1, pady=10)
        Label(self.custom_frame, text='Columns: ', font='Arial 12').grid(
            row=1, column=0, columnspan=1)
        self.columns_select = Spinbox(
            self.custom_frame, from_=4, to=50, width=3)
        self.columns_select.grid(row=1, column=1, columnspan=1, pady=10)

        self.custom_button = Button(window, text='CUSTOM', font='Arial 18 bold',
                                    command=functools.partial(self.start, 0, 0), width=12)
        self.custom_button.grid(row=3, column=0, columnspan=2, padx=10, pady=3)'''

    def start(self, rows, columns):
        root = Tk()
        game_gui = Chess.Chess(root)
        root.mainloop()


root = Tk()
menu_gui = Launcher(root)
root.mainloop()

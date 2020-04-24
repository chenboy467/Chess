from tkinter import *
import Pieces
import random
import functools
import time


class Chess:

    # Tiles
    pieces = {'white': [], 'black': []}
    labels = []
    tiles = []

    def __init__(self, window):
        # Window Properties
        self.window = window
        self.window.title('Chess')
        self.window.geometry("1000x666".format(
            self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.resizable(False, False)
        self.window.bind('<Escape>', self.toggle_fullscreen)

        # Main Canvas
        self.canvas = Canvas(window)
        self.canvas.place(relx=0.4, rely=0.5, anchor=CENTER)

        # Create tiles
        self.create_tiles()

        # Create pieces
        self.create_pieces()

    def toggle_fullscreen(self, event):
        # Toggle fullscreen
        self.window.attributes(
            '-fullscreen', not self.window.attributes('-fullscreen'))

    def create_tiles(self):
        # Fill tile lists with 0's
        self.tiles = [
            [0 for x in range(8)] for y in range(8)]
        self.labels = [
            ['' for x in range(8)] for y in range(8)]

        # Create frames as tiles on the main canvas
        # TODO: Fix frame deformation
        # TODO: Change frames to canvases
        # TODO: Add labels for rows and columns
        for x in range(8):
            for y in range(8):
                self.tiles[x][y] = Frame(
                    self.canvas, bg=('black', 'white')[(x+y) % 2], height=60, width=60)
                self.tiles[x][y].bind(
                    '<Button-1>', functools.partial(self.select, (x, y)))
                self.tiles[x][y].grid(
                    row=8-y, column=x+1, sticky='ew')
                self.labels[x][y] = Label(
                    self.tiles[x][y], text='    ', fg='red', bg=self.tiles[x][y].cget('bg'))
                self.labels[x][y].grid()
        numbers_frame = Frame(self.canvas, bg='white', height=60, width=60)
        numbers_frame.grid(row=0, column=0, rowspan=9, sticky='ew')
        for x in range(8):
            Label(numbers_frame, text='  ' + str(x+1) + ' ',
                  fg='red', bg='white').grid(row=8-x)
        letters_frame = Frame(self.canvas, bg='white', height=60, width=60)
        letters_frame.grid(row=9, column=1, columnspan=8, sticky='ew')
        for x in range(8):
            Label(letters_frame, text=('a', 'b', 'c', 'd', 'e', 'f',
                                       'g', 'h')[x], fg='red', bg='white').grid(row=0, column=x, padx=4)

    # TODO: Replace with a json file
    def create_pieces(self):
        # Add a new piece
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (1, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (2, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (3, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (4, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (5, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (6, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (7, 1)))
        for x in self.pieces['white']:
            self.labels[x.pos[0]][x.pos[1]].config(
                text=' ' + x.display + ' ')
        self.pieces['black'].append(Pieces.Pawn(False, (0, 6)))
        self.pieces['black'].append(Pieces.Pawn(False, (1, 6)))
        self.pieces['black'].append(Pieces.Pawn(False, (2, 6)))
        self.pieces['black'].append(Pieces.Pawn(False, (3, 6)))
        self.pieces['black'].append(Pieces.Pawn(False, (4, 6)))
        self.pieces['black'].append(Pieces.Pawn(False, (5, 6)))
        self.pieces['black'].append(Pieces.Pawn(False, (6, 6)))
        self.pieces['black'].append(Pieces.Pawn(False, (7, 6)))
        for x in self.pieces['black']:
            self.labels[x.pos[0]][x.pos[1]].config(
                text=' ' + x.display + ' ')

    def select(self, pos, event):
        print(str(pos))
        for x in self.pieces['white']:
            if x.pos == pos:
                print('HEllo')


root = Tk()
game_gui = Chess(root)
root.mainloop()

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
                self.tiles[x][y].grid(
                    row=8-y, column=x, sticky='ew')
                self.labels[x][y] = Label(
                    self.tiles[x][y], text='', fg='red', bg=self.tiles[x][y].cget('bg'))
                self.labels[x][y].grid()

    # TODO: Replace with a json file
    def create_pieces(self):
        # Add a new piece
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        self.pieces['white'].append(Pieces.Pawn(True, (0, 1)))
        for x in self.pieces['white']:
            self.labels[x.pos[0]][x.pos[1]].config(text=x.name)


root = Tk()
game_gui = Chess(root)
root.mainloop()

from tkinter import *
import Pieces
import random
import functools
import time


class Chess:

    # Tiles
    pieces = {'white': [], 'black': []}
    pieces_grid = {}
    '''for x in range(8):
        for y in range(8):
            # .clear will remove all elements in a dictionary
            pieces_grid[(x, y)] = None'''
    labels = []
    tiles = []
    selected_piece = None
    checkedTiles = [[], []]
    capturedPieces = [[], []]
    isWhiteTurn = True
    gameResult = None

    def __init__(self, window):
        # Window Properties
        self.window = window
        self.window.title('Chess')
        self.window.geometry('1000x666'.format(
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
                self.labels[x][y].bind(
                    '<Button-1>', functools.partial(self.select, (x, y)))
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
        self.captured_pieces_frame = Frame(
            self.window, height=120, width=300, bd=5)
        self.captured_pieces_frame.place(relx=0.5, rely=0.5, anchor=W)
        self.captured_pieces_labels = [Label(self.captured_pieces_frame, fg='brown'), Label(
            self.captured_pieces_frame, fg='silver')]
        self.captured_pieces_labels[0].pack(side=TOP, anchor=SW)
        self.captured_pieces_labels[1].pack(side=BOTTOM, anchor=NW)

    # TODO: Replace with a json file
    def create_pieces(self):
        # Kings
        self.pieces['white'].append(Pieces.King(True, (4, 0)))
        self.pieces['black'].append(Pieces.King(False, (4, 7)))

        # Pawns
        for x in range(8):
            self.pieces['white'].append(Pieces.Pawn(True, (x, 1)))
            #self.pieces['black'].append(Pieces.Pawn(False, (x, 6)))

        # White Pieces
        # TODO: Move List
        # TODO: Win Screen
        # TODO: Resign and draw
        # TODO: Clock
        #self.pieces['white'].append(Pieces.Knight(True, (1, 0)))
        #self.pieces['white'].append(Pieces.Knight(True, (6, 0)))
        #self.pieces['white'].append(Pieces.Bishop(True, (2, 0)))
        self.pieces['white'].append(Pieces.Bishop(True, (5, 0)))
        self.pieces['white'].append(Pieces.Rook(True, (0, 0)))
        #self.pieces['white'].append(Pieces.Rook(True, (7, 0)))
        self.pieces['white'].append(Pieces.Queen(True, (3, 0)))

        # Black Pieces
        #self.pieces['black'].append(Pieces.Knight(False, (1, 7)))
        #self.pieces['black'].append(Pieces.Knight(False, (6, 7)))
        #self.pieces['black'].append(Pieces.Bishop(False, (2, 7)))
        self.pieces['black'].append(Pieces.Bishop(False, (5, 7)))
        #self.pieces['black'].append(Pieces.Rook(False, (0, 7)))
        self.pieces['black'].append(Pieces.Rook(False, (7, 7)))
        self.pieces['black'].append(Pieces.Queen(False, (3, 7)))

        # TODO: Move this to end of turn
        # Show pieces
        for x in self.pieces['white']:
            self.pieces_grid[x.pos] = x
            self.labels[x.pos[0]][x.pos[1]].config(
                text=' ' + x.display + ' ', fg='silver')
        for x in self.pieces['black']:
            self.pieces_grid[x.pos] = x
            self.labels[x.pos[0]][x.pos[1]].config(
                text=' ' + x.display + ' ', fg='brown')

    def select(self, pos, event):
        if self.selected_piece != None and self.selected_piece.pos != pos:
            for x in self.selected_piece.getAvailableMoves(self.tiles, self.pieces, self.pieces_grid, self.checkedTiles[self.selected_piece.isWhite]):
                if pos == x:
                    # Move selected piece
                    capturedPiece = self.selected_piece.move(pos, self.pieces)
                    if capturedPiece != None:
                        self.capturedPieces[capturedPiece.isWhite].append(
                            capturedPiece.display)
                    self.updateCheck(True)
                    self.updateCheck(False)
                    self.pieces_grid.clear()
                    for y in self.pieces['white']:
                        self.pieces_grid[y.pos] = y
                        if y.name == 'Pawn' and y != self.selected_piece:
                            y.enPassantCapturable = False
                    for y in self.pieces['black']:
                        self.pieces_grid[y.pos] = y
                        if y.name == 'Pawn' and y != self.selected_piece:
                            y.enPassantCapturable = False
                    # self.selected_piece.pos = pos
                    if self.selected_piece.name == 'Pawn' and pos[1] == (0, 7)[self.selected_piece.isWhite]:
                        self.pieces[('black', 'white')[self.selected_piece.isWhite]][self.pieces[('black', 'white')[self.selected_piece.isWhite]].index(self.selected_piece)] = Pieces.Queen(
                            self.selected_piece.isWhite, pos)
                        self.pieces_grid[pos] = Pieces.Queen(
                            self.selected_piece.isWhite, pos)
                    self.selected_piece = None
                    self.isWhiteTurn = not self.isWhiteTurn
                    self.gameResult = self.tryEndGame()
                    if self.gameResult != None:
                        print(self.gameResult)
                    self.draw()
                    return

        for x in self.pieces['white']:
            if x.pos == pos:
                if self.selected_piece != x and self.isWhiteTurn:
                    '''    # Deselect piece if it has already been selected
                        self.selected_piece == None
                    else:'''
                    # Set new selected piece
                    # if self.selected_piece != None and self.selected_piece.isWhite == self.isWhiteTurn:
                    self.selected_piece = x
                else:
                    self.selected_piece = None
        for x in self.pieces['black']:
            if x.pos == pos:
                if self.selected_piece != x and not self.isWhiteTurn:
                    '''    # Deselect piece if it has already been selected
                        self.selected_piece == None
                    else:'''
                    # Set new selected piece
                    # if self.selected_piece != None and self.selected_piece.isWhite == self.isWhiteTurn:
                    self.selected_piece = x
                else:
                    self.selected_piece = None
        self.draw()

    def tryEndGame(self):
        if self.pieces['white'][0].underCheck > 0:
            for x in self.pieces['white']:
                if len(x.getAvailableMoves(self.tiles, self.pieces, self.pieces_grid, self.checkedTiles[x.isWhite])) > 0:
                    return
            return -1
        elif self.pieces['black'][0].underCheck > 0:
            for x in self.pieces['black']:
                if len(x.getAvailableMoves(self.tiles, self.pieces, self.pieces_grid, self.checkedTiles[x.isWhite])) > 0:
                    return
            return 1
        else:
            piecesLeftWhite = []
            piecesLeftBlack = []
            for x in self.pieces['white']:
                if x.name != 'King':
                    piecesLeftWhite.append(x.display)
            for x in self.pieces['black']:
                if x.name != 'King':
                    piecesLeftWhite.append(x.display)
            if len(piecesLeftWhite) >= 2 or len(piecesLeftWhite) >= 2:
                pass
            else:
                if ((len(piecesLeftWhite) == 0) or (piecesLeftWhite[0] != 'Q' and piecesLeftWhite[0] != 'R' and piecesLeftWhite[0] != 'P')) and ((len(piecesLeftWhite) == 0) or (piecesLeftBlack[0] != 'Q' and piecesLeftBlack[0] != 'R' and piecesLeftBlack[0] != 'P')):
                    return 0
            for x in self.pieces[('black', 'white')[self.isWhiteTurn]]:
                if len(x.getAvailableMoves(self.tiles, self.pieces, self.pieces_grid, self.checkedTiles[x.isWhite])) > 0:
                    return
            return 0

    def draw(self):
        for x in self.labels:
            for y in x:
                y.config(text='    ')
                if self.selected_piece != None:
                    y.config(bg=(('black', 'white')[
                        (self.labels.index(x)+self.labels[self.labels.index(x)].index(y)) % 2], 'yellow')[((self.labels.index(x), x.index(y)) == self.selected_piece.pos) or ((self.labels.index(x), x.index(y)) in self.selected_piece.getAvailableMoves(self.tiles, self.pieces, self.pieces_grid, self.checkedTiles[self.selected_piece.isWhite]))])
                else:
                    y.config(bg=('black', 'white')[
                        (self.labels.index(x)+self.labels[self.labels.index(x)].index(y)) % 2])
        # if self.selected_piece not None:
        #    self.labels[self.selected_piece[0]][self.selected_piece[1]].config(bg='yellow')
        for x in self.pieces['white']:
            if x.pos != None:
                self.labels[x.pos[0]][x.pos[1]].config(
                    text=' ' + x.display + ' ', fg='silver')
            if x.underCheck:
                self.labels[x.pos[0]][x.pos[1]].config(bg='red')
        for x in self.pieces['black']:
            if x.pos != None:
                self.labels[x.pos[0]][x.pos[1]].config(
                    text=' ' + x.display + ' ', fg='brown')
            if x.underCheck:
                self.labels[x.pos[0]][x.pos[1]].config(bg='red')
        self.captured_pieces_labels[0].config(text='')
        self.captured_pieces_labels[1].config(text='')
        for i in range(5):
            for x in self.capturedPieces[0]:
                if x == ('Q', 'R', 'B', 'N', 'P')[i]:
                    self.captured_pieces_labels[0].config(
                        text=self.captured_pieces_labels[0].cget('text') + ' ' + x)
            for x in self.capturedPieces[1]:
                if x == ('Q', 'R', 'B', 'N', 'P')[i]:
                    self.captured_pieces_labels[1].config(
                        text=self.captured_pieces_labels[1].cget('text') + ' ' + x)

    def updateCheck(self, isWhiteChecking):
        self.pieces[('white', 'black')[isWhiteChecking]][0].underCheck = 0
        checkedTiles = set()
        for i in self.pieces[('black', 'white')[isWhiteChecking]]:
            if self.pieces[('white', 'black')[isWhiteChecking]][0].pos in i.getAttackingTiles(self.tiles, self.pieces):
                self.pieces[('white', 'black')[isWhiteChecking]
                            ][0].underCheck += 1
            checkedTiles |= i.getAttackingTiles(self.tiles, self.pieces)
        # if self.pieces[('white', 'black')[isWhiteChecking]][0].pos in checkedTiles:
        self.checkedTiles[not isWhiteChecking] = checkedTiles


root = Tk()
game_gui = Chess(root)
root.mainloop()

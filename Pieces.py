class Piece:
    name = 'Piece'
    display = ''
    moves = []

    def __init__(self, isWhite, pos):
        self.isWhite = isWhite
        self.pos = pos
        pass

    def getAvailableMoves(self):
        pass

    def move(self, posX, posY):
        pass

    def captured(self):
        del self


class Pawn(Piece):
    name = 'Pawn'
    display = 'P'

    '''def __init__(self):
        super().__init__()

    def move(self):
        super().move()'''

    def getAvailableMoves(self, tilesList):
        availableMoves = set()
        for x in tilesList:
            for y in x:
                if self.isWhite:
                    if ((tilesList.index(x), x.index(
                            y) - 1) == self.pos) or ((tilesList.index(x), x.index(y) - 2) == self.pos and self.pos[1] == 1):
                        availableMoves.add((tilesList.index(x), x.index(y)))
                else:
                    if ((tilesList.index(x), x.index(
                            y) + 1) == self.pos) or ((tilesList.index(x), x.index(y) + 2) == self.pos and self.pos[1] == 6):
                        availableMoves.add((tilesList.index(x), x.index(y)))
        return availableMoves


class Knight(Piece):
    name = 'Knight'
    display = 'N'


class Bishop(Piece):
    name = 'Bishop'
    display = 'B'


class Rook(Piece):
    name = 'Rook'
    display = 'R'


class Queen(Piece):
    name = 'Queen'
    display = 'Q'


class King(Piece):
    name = 'King'
    display = 'K'

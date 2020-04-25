class Piece:
    name = 'Piece'
    display = ''

    def __init__(self, isWhite, pos):
        self.isWhite = isWhite
        self.pos = pos
        pass

    def show(self):
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

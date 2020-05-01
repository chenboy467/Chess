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

    def move(self, pos, piecesDict):
        self.pos = pos
        if self.isWhite:
            for i in piecesDict['black']:
                if (i.pos == pos):
                    i.pos = None
                    piecesDict['black'].remove(i)
        else:
            for i in piecesDict['white']:
                if (i.pos == pos):
                    i.pos = None
                    piecesDict['white'].remove(i)

    def captured(self):
        del self


class Pawn(Piece):
    name = 'Pawn'
    display = 'P'

    '''def __init__(self):
        super().__init__()

    def move(self):
        super().move()'''

    def getAvailableMoves(self, tilesList, piecesDict):
        availableMoves = set()
        if self.isWhite:
            # Check for capturable black pieces
            for i in piecesDict['black']:
                if (i.pos == (self.pos[0] - 1, self.pos[1] + 1)) or (i.pos == (self.pos[0] + 1, self.pos[1] + 1)):
                    availableMoves.add(i.pos)
            # Check for available tiles
            for x in tilesList:
                for y in x:
                    if ((tilesList.index(x), x.index(
                            y) - 1) == self.pos) or ((tilesList.index(x), x.index(y) - 2) == self.pos and self.pos[1] == 1):
                        availableMoves.add((tilesList.index(x), x.index(y)))
            # Check for pieces in the way
            for i in piecesDict['white']:
                if i.pos == (self.pos[0], self.pos[1] + 1):
                    if (i.pos in availableMoves):
                        availableMoves.remove(i.pos)
                    if ((i.pos[0], i.pos[1] + 1) in availableMoves):
                        availableMoves.remove((i.pos[0], i.pos[1] + 1))
                if i.pos == (self.pos[0], self.pos[1] + 2):
                    if (i.pos in availableMoves):
                        availableMoves.remove(i.pos)
            for i in piecesDict['black']:
                if i.pos == (self.pos[0], self.pos[1] + 1):
                    if (i.pos in availableMoves):
                        availableMoves.remove(i.pos)
                    if ((i.pos[0], i.pos[1] + 1) in availableMoves):
                        availableMoves.remove((i.pos[0], i.pos[1] + 1))
                if i.pos == (self.pos[0], self.pos[1] + 2):
                    if (i.pos in availableMoves):
                        availableMoves.remove(i.pos)
        else:
            for i in piecesDict['white']:
                if (i.pos == (self.pos[0] - 1, self.pos[1] - 1)) or (i.pos == (self.pos[0] + 1, self.pos[1] - 1)):
                    availableMoves.add(i.pos)
            for x in tilesList:
                for y in x:
                    if ((tilesList.index(x), x.index(
                            y) + 1) == self.pos) or ((tilesList.index(x), x.index(y) + 2) == self.pos and self.pos[1] == 6):
                        availableMoves.add((tilesList.index(x), x.index(y)))
            for i in piecesDict['black']:
                if i.pos == (self.pos[0], self.pos[1] - 1):
                    if (i.pos in availableMoves):
                        availableMoves.remove(i.pos)
                    if ((i.pos[0], i.pos[1] - 1) in availableMoves):
                        availableMoves.remove((i.pos[0], i.pos[1] - 1))
                if i.pos == (self.pos[0], self.pos[1] - 2):
                    if (i.pos in availableMoves):
                        availableMoves.remove(i.pos)
            for i in piecesDict['white']:
                if i.pos == (self.pos[0], self.pos[1] - 1):
                    if (i.pos in availableMoves):
                        availableMoves.remove(i.pos)
                    if ((i.pos[0], i.pos[1] - 1) in availableMoves):
                        availableMoves.remove((i.pos[0], i.pos[1] - 1))
                if i.pos == (self.pos[0], self.pos[1] - 2):
                    if (i.pos in availableMoves):
                        availableMoves.remove(i.pos)
        return availableMoves


class Knight(Piece):
    name = 'Knight'
    display = 'N'

    def getAvailableMoves(self, tilesList, piecesDict):
        availableMoves = set()
        for x in tilesList:
            for y in x:
                if (abs(tilesList.index(x) - self.pos[0]) == 1 and abs(x.index(y) - self.pos[1]) == 2) or (abs(tilesList.index(x) - self.pos[0]) == 2 and abs(x.index(y) - self.pos[1]) == 1):
                    availableMoves.add((tilesList.index(x), x.index(y)))
        for i in piecesDict[('black', 'white')[self.isWhite]]:
            if (abs(i.pos[0] - self.pos[0]) == 1 and abs(i.pos[1] - self.pos[1]) == 2) or (abs(i.pos[0] - self.pos[0]) == 2 and abs(i.pos[1] - self.pos[1]) == 1):
                if (i.pos in availableMoves):
                    availableMoves.remove(i.pos)
        return availableMoves


class Bishop(Piece):
    name = 'Bishop'
    display = 'B'

    def getAvailableMoves(self, tilesList, piecesDict):
        availableMoves = set()
        for x in tilesList:
            for y in x:
                if abs(tilesList.index(x) - self.pos[0]) == abs(x.index(y) - self.pos[1]):
                    availableMoves.add((tilesList.index(x), x.index(y)))
        toRemove = set()
        for i in piecesDict[('black', 'white')[self.isWhite]]:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1]:
                for x in availableMoves:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemove.add(x)
        for i in piecesDict[('white', 'black')[self.isWhite]]:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1]:
                for x in availableMoves:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemove.add(x)
        return availableMoves - toRemove


class Rook(Piece):
    name = 'Rook'
    display = 'R'


class Queen(Piece):
    name = 'Queen'
    display = 'Q'


class King(Piece):
    name = 'King'
    display = 'K'

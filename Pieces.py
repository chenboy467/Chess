class Piece:
    name = 'Piece'
    display = ''
    moves = []

    def __init__(self, isWhite, pos):
        self.isWhite = isWhite
        self.pos = pos

    def getAvailableMoves(self):
        return set()

    def getAttackingTiles(self):
        return self.getAvailableMoves()

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

    def getAttackingTiles(self, tilesList, piecesDict):
        attackingTiles = set()
        if self.isWhite:
            attackingTiles.add((self.pos[0] - 1, self.pos[1] + 1))
            attackingTiles.add((self.pos[0] + 1, self.pos[1] + 1))
        else:
            attackingTiles.add((self.pos[0] - 1, self.pos[1] - 1))
            attackingTiles.add((self.pos[0] + 1, self.pos[1] - 1))
        '''for x in tilesList:
            if self.isWhite:
                if (x == (self.pos[0] - 1, self.pos[1] + 1)) or (x == (self.pos[0] + 1, self.pos[1] + 1)):
                    attackingTiles.add(x)
            else:
                if (x == (self.pos[0] - 1, self.pos[1] - 1)) or (x == (self.pos[0] + 1, self.pos[1] - 1)):
                    attackingTiles.add(x)'''
        return attackingTiles


class Knight(Piece):
    name = 'Knight'
    display = 'N'

    def getAvailableMoves(self, tilesList, piecesDict):
        availableMoves = set()
        # Check for available tiles
        for x in tilesList:
            for y in x:
                if (abs(tilesList.index(x) - self.pos[0]) == 1 and abs(x.index(y) - self.pos[1]) == 2) or (abs(tilesList.index(x) - self.pos[0]) == 2 and abs(x.index(y) - self.pos[1]) == 1):
                    availableMoves.add((tilesList.index(x), x.index(y)))
        for i in piecesDict[('black', 'white')[self.isWhite]]:
            if (abs(i.pos[0] - self.pos[0]) == 1 and abs(i.pos[1] - self.pos[1]) == 2) or (abs(i.pos[0] - self.pos[0]) == 2 and abs(i.pos[1] - self.pos[1]) == 1):
                if (i.pos in availableMoves):
                    availableMoves.remove(i.pos)
        return availableMoves

    def getAttackingTiles(self, tilesList, piecesDict):
        attackingTiles = set()
        attackingTiles.add((self.pos[0] - 1, self.pos[1] - 2))
        attackingTiles.add((self.pos[0] - 1, self.pos[1] + 2))
        attackingTiles.add((self.pos[0] + 1, self.pos[1] - 2))
        attackingTiles.add((self.pos[0] + 1, self.pos[1] + 2))
        attackingTiles.add((self.pos[0] - 2, self.pos[1] - 1))
        attackingTiles.add((self.pos[0] - 2, self.pos[1] + 1))
        attackingTiles.add((self.pos[0] + 2, self.pos[1] - 1))
        attackingTiles.add((self.pos[0] + 2, self.pos[1] + 1))
        '''for x in tilesList:
            for y in x:
                if (abs(tilesList.index(x) - self.pos[0]) == 1 and abs(x.index(y) - self.pos[1]) == 2) or (abs(tilesList.index(x) - self.pos[0]) == 2 and abs(x.index(y) - self.pos[1]) == 1):
                    attackingTiles.add((tilesList.index(x), x.index(y)))'''
        return attackingTiles


class Bishop(Piece):
    name = 'Bishop'
    display = 'B'

    def getAvailableMoves(self, tilesList, piecesDict):
        availableMoves = set()
        # Check for available tiles
        for x in tilesList:
            for y in x:
                if abs(tilesList.index(x) - self.pos[0]) == abs(x.index(y) - self.pos[1]):
                    availableMoves.add((tilesList.index(x), x.index(y)))
        toRemove = set()
        # Check for pieces in the way
        for i in piecesDict[('black', 'white')[self.isWhite]]:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1]:
                # Add tiles that are behind the roadblock piece to toRemove
                for x in availableMoves:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemove.add(x)
        for i in piecesDict[('white', 'black')[self.isWhite]]:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1]:
                for x in availableMoves:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemove.add(x)
        return availableMoves - toRemove

    def getAttackingTiles(self, tilesList, piecesDict):
        attackingTiles = set()
        for x in range(1, 7):
            attackingTiles.add((self.pos[0] - x, self.pos[1] - x))
            attackingTiles.add((self.pos[0] - x, self.pos[1] + x))
            attackingTiles.add((self.pos[0] + x, self.pos[1] - x))
            attackingTiles.add((self.pos[0] + x, self.pos[1] + x))
            toRemove = set()
        # Check for pieces in the way
        for i in piecesDict['white']:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1]:
                # Add tiles that are behind the roadblock piece to toRemove
                for x in availableMoves:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemove.add(x)
        for i in piecesDict['black']:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1]:
                for x in availableMoves:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemove.add(x)
        return attackingTiles - toRemove


class Rook(Piece):
    name = 'Rook'
    display = 'R'

    def getAvailableMoves(self, tilesList, piecesDict):
        availableMoves = set()
        # Check for available tiles
        for x in tilesList:
            for y in x:
                if (tilesList.index(x) == self.pos[0]) or (x.index(y) == self.pos[1]):
                    availableMoves.add((tilesList.index(x), x.index(y)))
        toRemove = set()
        # Check for pieces in the way
        for i in piecesDict[('black', 'white')[self.isWhite]]:
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in availableMoves:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1):
                            toRemove.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1):
                            toRemove.add(x)
        for i in piecesDict[('white', 'black')[self.isWhite]]:
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]):
                for x in availableMoves:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1):
                            toRemove.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1):
                            toRemove.add(x)
        return availableMoves - toRemove

    def getAttackingTiles(self, tilesList, piecesDict):
        attackingTiles = set()
        for x in range(1, 7):
            attackingTiles.add((self.pos[0] - x, self.pos[1]))
            attackingTiles.add((self.pos[0] + x, self.pos[1]))
            attackingTiles.add((self.pos[0], self.pos[1] - x))
            attackingTiles.add((self.pos[0], self.pos[1] + x))
            toRemove = set()
        # Check for pieces in the way
        for i in piecesDict['white']:
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in availableMoves:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1):
                            toRemove.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1):
                            toRemove.add(x)
        for i in piecesDict['black']:
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in availableMoves:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1):
                            toRemove.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1):
                            toRemove.add(x)
        return attackingTiles - toRemove


class Queen(Piece):
    name = 'Queen'
    display = 'Q'

    def getAvailableMoves(self, tilesList, piecesDict):
        availableMovesDiagonal = set()
        availableMovesStraight = set()
        # Check for available tiles
        for x in tilesList:
            for y in x:
                # Diagonals
                if abs(tilesList.index(x) - self.pos[0]) == abs(x.index(y) - self.pos[1]):
                    availableMovesDiagonal.add(
                        (tilesList.index(x), x.index(y)))
                # Horizontal & Vertical
                if (tilesList.index(x) == self.pos[0]) or (x.index(y) == self.pos[1]):
                    availableMovesStraight.add(
                        (tilesList.index(x), x.index(y)))
        toRemoveDiagonal = set()
        # Check for pieces in the way
        for i in piecesDict[('black', 'white')[self.isWhite]]:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1]:
                # Add tiles that are behind the roadblock piece to toRemove
                for x in availableMovesDiagonal:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemoveDiagonal.add(x)
        for i in piecesDict[('white', 'black')[self.isWhite]]:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1]:
                for x in availableMovesDiagonal:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemoveDiagonal.add(x)
        toRemoveStraight = set()
        # Check for pieces in the way
        for i in piecesDict[('black', 'white')[self.isWhite]]:
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in availableMovesStraight:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1):
                            toRemoveStraight.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1):
                            toRemoveStraight.add(x)
        for i in piecesDict[('white', 'black')[self.isWhite]]:
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]):
                for x in availableMovesStraight:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1):
                            toRemoveStraight.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1):
                            toRemoveStraight.add(x)
        return (availableMovesDiagonal | availableMovesStraight) - toRemoveDiagonal - toRemoveStraight

    # TODO: Queen's getAttackingTiles()


class King(Piece):
    name = 'King'
    display = 'K'

    def getAvailableMoves(self, tilesList, piecesDict):
        availableMoves = set()
        # Check for available tiles
        for x in tilesList:
            for y in x:
                if abs(tilesList.index(x) - self.pos[0]) <= 1 and abs(x.index(y) - self.pos[1]) <= 1:
                    availableMoves.add((tilesList.index(x), x.index(y)))
        for i in piecesDict[('black', 'white')[self.isWhite]]:
            if abs(i.pos[0] - self.pos[0]) <= 1 and abs(i.pos[1] - self.pos[1]) <= 1:
                if (i.pos in availableMoves):
                    availableMoves.remove(i.pos)
        checkTiles = set()
        for i in piecesDict[('white', 'black')[self.isWhite]]:
            for x in availableMoves:
                if i.name == 'King':
                    if abs(x[0] - i.pos[0]) <= 1 and abs(x[1] - i.pos[1]) <= 1:
                        checkTiles.add(x)
                else:
                    if x in i.getAvailableMoves(tilesList, piecesDict):
                        checkTiles.add(x)
        return availableMoves - checkTiles

    def getAttackingTiles(self, tilesList, piecesDict):
        attackingTiles = set()
        for x in range(3):
            for y in range(3):
                if (x - 1) or (y - 1):
                    attackingTiles.add(
                        (self.pos[0] + x - 1, self.pos[1] + y - 1))
        '''for x in tilesList:
            for y in x:
                if (abs(tilesList.index(x) - self.pos[0]) == 1 and abs(x.index(y) - self.pos[1]) == 2) or (abs(tilesList.index(x) - self.pos[0]) == 2 and abs(x.index(y) - self.pos[1]) == 1):
                    attackingTiles.add((tilesList.index(x), x.index(y)))'''
        return attackingTiles

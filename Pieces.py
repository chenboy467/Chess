

class Piece:
    name = 'Piece'
    display = ''
    moves = []
    underCheck = 0

    def __init__(self, isWhite, pos):
        self.isWhite = isWhite
        self.pos = pos

    def getAvailableMoves(self):
        return set()

    def getAttackingTiles(self):
        return self.getAvailableMoves()

    '''def updateCheckForCheck(self, tilesList, piecesDict, testPiecesPos):
        piecesDict[('black', 'white')[not self.isWhite]][0].underCheck = 0
        checkedTiles = set()
        for i in piecesDict[('black', 'white')[not self.isWhite]]:
            checkedTiles |= i.getAttackingTiles(tilesList, piecesDict)
        if piecesDict[('white', 'black')[not self.isWhite]][0].pos in checkedTiles:
            return True
        else:
            return False'''

    def checkForCheck(self, tilesList, piecesDict, piecesGridDict, currentAvailableMoves):
        '''if piecesDict[('black', 'white')[self.isWhite]][0].underCheck:
            toRemove = set()
            for x in availableMoves:
                testPiecesPos = dict()
                for y in piecesDict['white']:
                    testPiecesPos['white'].append(y.pos)
                for y in piecesDict['black']:
                    testPiecesPos['black'].append(y.pos)
                testPiecesPos[('black', 'white')[
                               self.isWhite]].remove(self.pos)
                testPiecesPos[('black', 'white')[self.isWhite]].append(x)
                if self.updateCheckForCheck(tilesList, testPiecesPos):
                    toRemove.add(x)
        return availableMoves - toRemove'''

        availableMoves = set()
        if piecesDict[('black', 'white')[self.isWhite]][0].underCheck == 1:
            # Check to see if King will be in check after piece is moved away
            for i in currentAvailableMoves:
                if i[0] == piecesDict[('black', 'white')[self.isWhite]][0].pos[0]:
                    if i[1] > piecesDict[('black', 'white')[self.isWhite]][0].pos[1]:
                        for x in range(i[1], 8):
                            if (i[0], x) in piecesGridDict:
                                if ((piecesGridDict[(i[0], x)].name == 'Rook') or (piecesGridDict[(i[0], x)].name == 'Queen')) and piecesGridDict[(i[0], x)].isWhite != self.isWhite:
                                    availableMoves.add(i)
                    else:
                        for x in range(0, i[1] + 1):
                            if (i[0], x) in piecesGridDict:
                                if ((piecesGridDict[(i[0], x)].name == 'Rook') or (piecesGridDict[(i[0], x)].name == 'Queen')) and piecesGridDict[(i[0], x)].isWhite != self.isWhite:
                                    availableMoves.add(i)
                elif i[1] == piecesDict[('black', 'white')[self.isWhite]][0].pos[1]:
                    if i[0] > piecesDict[('black', 'white')[self.isWhite]][0].pos[0]:
                        '''for x in range(piecesDict[('black', 'white')[self.isWhite]][0].pos[0] + 1, i[0]):
                            if (x, i[1]) in piecesGridDict:
                                availableMoves.add(i)'''
                        for x in range(i[0], 8):
                            if (x, i[1]) in piecesGridDict:
                                if ((piecesGridDict[(x, i[1])].name == 'Rook') or (piecesGridDict[(x, i[1])].name == 'Queen')) and piecesGridDict[(x, i[1])].isWhite != self.isWhite:
                                    '''for y in availableMoves:
                                        if y[1] != i[1]:
                                            toRemove.add(y)'''
                                    availableMoves.add(i)
                    else:
                        '''for x in range(i[0] + 1, piecesDict[('black', 'white')[self.isWhite]][0].pos[0]):
                            if (x, i[1]) in piecesGridDict:
                                availableMoves.add(i)'''
                        for x in range(0, i[0] + 1):
                            if (x, i[1]) in piecesGridDict:
                                if ((piecesGridDict[(x, i[1])].name == 'Rook') or (piecesGridDict[(x, i[1])].name == 'Queen')) and piecesGridDict[(x, i[1])].isWhite != self.isWhite:
                                    '''for y in availableMoves:
                                        if y[1] != i[1]:
                                            toRemove.add(y)'''
                                    availableMoves.add(i)
                else:
                    if abs((i[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0]) / (i[1] - piecesDict[('black', 'white')[self.isWhite]][0].pos[1])) == 1:
                        if i[0] > piecesDict[('black', 'white')[self.isWhite]][0].pos[0]:
                            if i[1] > piecesDict[('black', 'white')[self.isWhite]][0].pos[1]:
                                '''for x in range(1, abs(i[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0])):
                                    if (i[0] - x, i[1] - x) in piecesGridDict:
                                        availableMoves.add(i)'''
                                for x in range(0, 8):
                                    if (i[0] + x, i[1] + x) in piecesGridDict:
                                        if ((piecesGridDict[(i[0] + x, i[1] + x)].name == 'Bishop') or (piecesGridDict[(i[0] + x, i[1] + x)].name == 'Queen')) and piecesGridDict[(i[0] + x, i[1] + x)].isWhite != self.isWhite:
                                            '''for y in availableMoves:
                                                if (y[0] == i[0]) or (y[1] == i[1]) or (abs((y[0] - i[0]) / (y[1] - i[1])) != 1) or not ((y[0] - i[0]) > 0 and (y[1] - i[1]) > 0):
                                                    toRemove.add(y)
                                            availableMoves -= toRemove'''
                                            availableMoves.add(i)
                            else:
                                '''for x in range(1, abs(i[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0])):
                                    if (i[0] - x, i[1] + x) in piecesGridDict:
                                        availableMoves.add(i)'''
                                for x in range(0, 8):
                                    if (i[0] + x, i[1] - x) in piecesGridDict:
                                        if ((piecesGridDict[(i[0] + x, i[1] - x)].name == 'Bishop') or (piecesGridDict[(i[0] + x, i[1] - x)].name == 'Queen')) and piecesGridDict[(i[0] + x, i[1] - x)].isWhite != self.isWhite:
                                            '''for y in availableMoves:
                                                if (y[0] == i[0]) or (y[1] == i[1]) or (abs((y[0] - i[0]) / (y[1] - i[1])) != 1) or not ((y[0] - i[0]) > 0 and (y[1] - i[1]) > 0):
                                                    toRemove.add(y)
                                            availableMoves -= toRemove'''
                                            availableMoves.add(i)
                        else:
                            if i[1] > piecesDict[('black', 'white')[self.isWhite]][0].pos[1]:
                                '''for x in range(1, abs(i[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0])):
                                    if (i[0] + x, i[1] - x) in piecesGridDict:
                                        availableMoves.add(i)'''
                                for x in range(0, 8):
                                    if (i[0] - x, i[1] + x) in piecesGridDict:
                                        if ((piecesGridDict[(i[0] - x, i[1] + x)].name == 'Bishop') or (piecesGridDict[(i[0] - x, i[1] + x)].name == 'Queen')) and piecesGridDict[(i[0] - x, i[1] + x)].isWhite != self.isWhite:
                                            '''for y in availableMoves:
                                                if (y[0] == i[0]) or (y[1] == i[1]) or (abs((y[0] - i[0]) / (y[1] - i[1])) != 1) or not ((y[0] - i[0]) > 0 and (y[1] - i[1]) > 0):
                                                    toRemove.add(y)
                                            availableMoves -= toRemove'''
                                            availableMoves.add(i)
                            else:
                                '''for x in range(1, abs(i[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0])):
                                    if (i[0] + x, i[1] + x) in piecesGridDict:
                                        availableMoves.add(i)'''
                                for x in range(0, 8):
                                    if (i[0] - x, i[1] - x) in piecesGridDict:
                                        if ((piecesGridDict[(i[0] - x, i[1] - x)].name == 'Bishop') or (piecesGridDict[(i[0] - x, i[1] - x)].name == 'Queen')) and piecesGridDict[(i[0] - x, i[1] - x)].isWhite != self.isWhite:
                                            '''for y in availableMoves:
                                                if (y[0] == i[0]) or (y[1] == i[1]) or (abs((y[0] - i[0]) / (y[1] - i[1])) != 1) or not ((y[0] - i[0]) > 0 and (y[1] - i[1]) > 0):
                                                    toRemove.add(y)
                                            availableMoves -= toRemove'''
                                            availableMoves.add(i)
        return availableMoves

    def checkForPin(self, tilesList, piecesDict, piecesGridDict, currentAvailableMoves):
        availableMoves = currentAvailableMoves
        # Check to see if King will be in check after piece is moved away
        if self.pos[0] == piecesDict[('black', 'white')[self.isWhite]][0].pos[0]:
            if self.pos[1] > piecesDict[('black', 'white')[self.isWhite]][0].pos[1]:
                for x in range(piecesDict[('black', 'white')[self.isWhite]][0].pos[1] + 1, self.pos[1]):
                    if (self.pos[0], x) in piecesGridDict:
                        return availableMoves
                for x in range(self.pos[1] + 1, 8):
                    if (self.pos[0], x) in piecesGridDict:
                        if ((piecesGridDict[(self.pos[0], x)].name == 'Rook') or (piecesGridDict[(self.pos[0], x)].name == 'Queen')) and piecesGridDict[(self.pos[0], x)].isWhite != self.isWhite:
                            toRemove = set()
                            for y in availableMoves:
                                if y[0] != self.pos[0]:
                                    toRemove.add(y)
                            availableMoves -= toRemove
                        else:
                            return availableMoves
            else:
                for x in range(self.pos[1] + 1, piecesDict[('black', 'white')[self.isWhite]][0].pos[1]):
                    if (self.pos[0], x) in piecesGridDict:
                        return availableMoves
                for x in range(0, self.pos[1]):
                    if (self.pos[0], x) in piecesGridDict:
                        if ((piecesGridDict[(self.pos[0], x)].name == 'Rook') or (piecesGridDict[(self.pos[0], x)].name == 'Queen')) and piecesGridDict[(self.pos[0], x)].isWhite != self.isWhite:
                            toRemove = set()
                            for y in availableMoves:
                                if y[0] != self.pos[0]:
                                    toRemove.add(y)
                            availableMoves -= toRemove
                        else:
                            return availableMoves
        elif self.pos[1] == piecesDict[('black', 'white')[self.isWhite]][0].pos[1]:
            if self.pos[0] > piecesDict[('black', 'white')[self.isWhite]][0].pos[0]:
                for x in range(piecesDict[('black', 'white')[self.isWhite]][0].pos[0] + 1, self.pos[0]):
                    if (x, self.pos[1]) in piecesGridDict:
                        return availableMoves
                for x in range(self.pos[0] + 1, 8):
                    if (x, self.pos[1]) in piecesGridDict:
                        if ((piecesGridDict[(x, self.pos[1])].name == 'Rook') or (piecesGridDict[(x, self.pos[1])].name == 'Queen')) and piecesGridDict[(x, self.pos[1])].isWhite != self.isWhite:
                            toRemove = set()
                            for y in availableMoves:
                                if y[1] != self.pos[1]:
                                    toRemove.add(y)
                            availableMoves -= toRemove
                        else:
                            return availableMoves
            else:
                for x in range(self.pos[0] + 1, piecesDict[('black', 'white')[self.isWhite]][0].pos[0]):
                    if (x, self.pos[1]) in piecesGridDict:
                        return availableMoves
                for x in range(0, self.pos[0]):
                    if (x, self.pos[1]) in piecesGridDict:
                        if ((piecesGridDict[(x, self.pos[1])].name == 'Rook') or (piecesGridDict[(x, self.pos[1])].name == 'Queen')) and piecesGridDict[(x, self.pos[1])].isWhite != self.isWhite:
                            toRemove = set()
                            for y in availableMoves:
                                if y[1] != self.pos[1]:
                                    toRemove.add(y)
                            availableMoves -= toRemove
                        else:
                            return availableMoves
        else:
            if abs((self.pos[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0]) / (self.pos[1] - piecesDict[('black', 'white')[self.isWhite]][0].pos[1])) == 1:
                if self.pos[0] > piecesDict[('black', 'white')[self.isWhite]][0].pos[0]:
                    if self.pos[1] > piecesDict[('black', 'white')[self.isWhite]][0].pos[1]:
                        for x in range(1, abs(self.pos[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0])):
                            if (self.pos[0] - x, self.pos[1] - x) in piecesGridDict:
                                return availableMoves
                        for x in range(1, 8):
                            if (self.pos[0] + x, self.pos[1] + x) in piecesGridDict:
                                if ((piecesGridDict[(self.pos[0] + x, self.pos[1] + x)].name == 'Bishop') or (piecesGridDict[(self.pos[0] + x, self.pos[1] + x)].name == 'Queen')) and piecesGridDict[(self.pos[0] + x, self.pos[1] + x)].isWhite != self.isWhite:
                                    toRemove = set()
                                    for y in availableMoves:
                                        if (y[0] == self.pos[0]) or (y[1] == self.pos[1]) or (abs((y[0] - self.pos[0]) / (y[1] - self.pos[1])) != 1) or not ((y[0] - self.pos[0]) > 0 and (y[1] - self.pos[1]) > 0):
                                            toRemove.add(y)
                                    availableMoves -= toRemove
                                else:
                                    return availableMoves
                    else:
                        for x in range(1, abs(self.pos[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0])):
                            if (self.pos[0] - x, self.pos[1] + x) in piecesGridDict:
                                return availableMoves
                        for x in range(1, 8):
                            if (self.pos[0] + x, self.pos[1] - x) in piecesGridDict:
                                if ((piecesGridDict[(self.pos[0] + x, self.pos[1] - x)].name == 'Bishop') or (piecesGridDict[(self.pos[0] + x, self.pos[1] - x)].name == 'Queen')) and piecesGridDict[(self.pos[0] + x, self.pos[1] - x)].isWhite != self.isWhite:
                                    toRemove = set()
                                    for y in availableMoves:
                                        if (y[0] == self.pos[0]) or (y[1] == self.pos[1]) or (abs((y[0] - self.pos[0]) / (y[1] - self.pos[1])) != 1) or not ((y[0] - self.pos[0]) > 0 and (y[1] - self.pos[1]) < 0):
                                            toRemove.add(y)
                                    availableMoves -= toRemove
                                else:
                                    return availableMoves
                else:
                    if self.pos[1] > piecesDict[('black', 'white')[self.isWhite]][0].pos[1]:
                        for x in range(1, abs(self.pos[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0])):
                            if (self.pos[0] + x, self.pos[1] - x) in piecesGridDict:
                                return availableMoves
                        for x in range(1, 8):
                            if (self.pos[0] - x, self.pos[1] + x) in piecesGridDict:
                                if ((piecesGridDict[(self.pos[0] - x, self.pos[1] + x)].name == 'Bishop') or (piecesGridDict[(self.pos[0] - x, self.pos[1] + x)].name == 'Queen')) and piecesGridDict[(self.pos[0] - x, self.pos[1] + x)].isWhite != self.isWhite:
                                    toRemove = set()
                                    for y in availableMoves:
                                        if (y[0] == self.pos[0]) or (y[1] == self.pos[1]) or (abs((y[0] - self.pos[0]) / (y[1] - self.pos[1])) != 1) or not ((y[0] - self.pos[0]) < 0 and (y[1] - self.pos[1]) > 0):
                                            toRemove.add(y)
                                    availableMoves -= toRemove
                                else:
                                    return availableMoves
                    else:
                        for x in range(1, abs(self.pos[0] - piecesDict[('black', 'white')[self.isWhite]][0].pos[0])):
                            if (self.pos[0] + x, self.pos[1] + x) in piecesGridDict:
                                return availableMoves
                        for x in range(1, 8):
                            if (self.pos[0] - x, self.pos[1] - x) in piecesGridDict:
                                if ((piecesGridDict[(self.pos[0] - x, self.pos[1] - x)].name == 'Bishop') or (piecesGridDict[(self.pos[0] - x, self.pos[1] - x)].name == 'Queen')) and piecesGridDict[(self.pos[0] - x, self.pos[1] - x)].isWhite != self.isWhite:
                                    toRemove = set()
                                    for y in availableMoves:
                                        if (y[0] == self.pos[0]) or (y[1] == self.pos[1]) or (abs((y[0] - self.pos[0]) / (y[1] - self.pos[1])) != 1) or not ((y[0] - self.pos[0]) < 0 and (y[1] - self.pos[1]) < 0):
                                            toRemove.add(y)
                                    availableMoves -= toRemove
                                else:
                                    return availableMoves
        return availableMoves

    def move(self, pos, piecesDict):
        if self.name == 'Pawn' and abs(self.pos[1] - pos[1]) == 2:
            self.enPassantCapturable = True
        if (self.name == 'Rook') or (self.name == 'King'):
            self.hasMoved = True
        capturedPiece = None
        if self.isWhite:
            for i in piecesDict['black']:
                if (i.pos == pos):
                    i.pos = None
                    piecesDict['black'].remove(i)
                    capturedPiece = i
                elif (self.name == 'Pawn') and i.pos == (pos[0], pos[1] - 1) and i.enPassantCapturable:
                    piecesDict['black'].remove(i)
                    capturedPiece = i
            if self.name == 'King' and abs(self.pos[0] - pos[0]) == 2:
                for i in piecesDict['white']:
                    if i.name == 'Rook':
                        if i.pos == (pos[0] + 1, pos[1]):
                            i.move((pos[0] - 1, pos[1]),
                                   piecesDict)
                        elif i.pos == (pos[0] - 2, pos[1]):
                            i.move((pos[0] + 1, pos[1]),
                                   piecesDict)
        else:
            for i in piecesDict['white']:
                if (i.pos == pos):
                    i.pos = None
                    piecesDict['white'].remove(i)
                    capturedPiece = i
                elif (self.name == 'Pawn') and i.pos == (pos[0], pos[1] + 1) and i.enPassantCapturable:
                    piecesDict['white'].remove(i)
                    capturedPiece = i
            if self.name == 'King' and abs(self.pos[0] - pos[0]) == 2:
                for i in piecesDict['black']:
                    if i.name == 'Rook':
                        if i.pos == (pos[0] + 1, pos[1]):
                            i.move((pos[0] - 1, pos[1]),
                                   piecesDict)
                        elif i.pos == (pos[0] - 2, pos[1]):
                            i.move((pos[0] + 1, pos[1]),
                                   piecesDict)
        self.pos = pos
        return capturedPiece

    def captured(self):
        del self


class Pawn(Piece):
    name = 'Pawn'
    display = 'P'
    enPassantCapturable = False

    '''def __init__(self):
        super().__init__()

    def move(self):
        super().move()'''

    def getAvailableMoves(self, tilesList, piecesDict, piecesGridDict, checkedTiles):
        availableMoves = set()
        if self.isWhite:
            # Check for capturable black pieces
            for i in piecesDict['black']:
                if (i.pos == (self.pos[0] - 1, self.pos[1] + 1)) or (i.pos == (self.pos[0] + 1, self.pos[1] + 1)):
                    availableMoves.add(i.pos)
                if ((i.pos == (self.pos[0] - 1, self.pos[1])) or (i.pos == (self.pos[0] + 1, self.pos[1]))) and i.name == 'Pawn' and i.enPassantCapturable:
                    availableMoves.add((i.pos[0], i.pos[1] + 1))
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
                if ((i.pos == (self.pos[0] - 1, self.pos[1])) or (i.pos == (self.pos[0] + 1, self.pos[1]))) and i.name == 'Pawn' and i.enPassantCapturable:
                    availableMoves.add((i.pos[0], i.pos[1] - 1))
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
        if piecesDict[('black', 'white')[self.isWhite]][0].underCheck:
            return self.checkForCheck(tilesList, piecesDict, piecesGridDict, self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMoves))
        else:
            return self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMoves)

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

    def getAvailableMoves(self, tilesList, piecesDict, piecesGridDict, checkedTiles):
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
        if piecesDict[('black', 'white')[self.isWhite]][0].underCheck:
            return self.checkForCheck(tilesList, piecesDict, piecesGridDict, self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMoves))
        else:
            return self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMoves)

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

    def getAvailableMoves(self, tilesList, piecesDict, piecesGridDict, checkedTiles):
        availableMoves = set()
        # Check for available tiles
        for x in tilesList:
            for y in x:
                if abs(tilesList.index(x) - self.pos[0]) == abs(x.index(y) - self.pos[1]):
                    availableMoves.add((tilesList.index(x), x.index(y)))
        toRemove = set()
        # Check for pieces in the way
        '''for x in availableMoves:
            if piecesGridDict[x] != None and x != self.pos:
                for y in availableMoves:
                    if ((y[0] - self.pos[0]) / (piecesGridDict[x].pos[0] - self.pos[0]) >= 1 and (y[1] - self.pos[1]) / (piecesGridDict[x].pos[1] - self.pos[1]) >= 1) and (y[0] - self.pos[0]) / (piecesGridDict[x].pos[0] - self.pos[0]) == (y[1] - self.pos[1]) / (piecesGridDict[x].pos[1] - self.pos[1]):
                        toRemove.add(x)'''
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
        if (self.pos in availableMoves):
            availableMoves.remove(self.pos)
        if piecesDict[('black', 'white')[self.isWhite]][0].underCheck:
            return self.checkForCheck(tilesList, piecesDict, piecesGridDict, self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMoves)) - toRemove
        else:
            return self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMoves) - toRemove

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
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1] and (i.name != 'King' or self.isWhite):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in attackingTiles:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemove.add(x)
        for i in piecesDict['black']:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1] and (i.name != 'King' or not self.isWhite):
                for x in attackingTiles:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemove.add(x)
        return attackingTiles - toRemove


class Rook(Piece):
    name = 'Rook'
    display = 'R'
    hasMoved = False

    def getAvailableMoves(self, tilesList, piecesDict, piecesGridDict, checkedTiles):
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
        if (self.pos in availableMoves):
            availableMoves.remove(self.pos)
        if piecesDict[('black', 'white')[self.isWhite]][0].underCheck:
            return self.checkForCheck(tilesList, piecesDict, piecesGridDict, self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMoves)) - toRemove
        else:
            return self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMoves) - toRemove

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
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]) and (i.name != 'King' or self.isWhite):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in attackingTiles:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1):
                            toRemove.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1):
                            toRemove.add(x)
        for i in piecesDict['black']:
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]) and (i.name != 'King' or not self.isWhite):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in attackingTiles:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1):
                            toRemove.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1):
                            toRemove.add(x)
        return attackingTiles - toRemove


class Queen(Piece):
    name = 'Queen'
    display = 'Q'

    def getAvailableMoves(self, tilesList, piecesDict, piecesGridDict, checkedTiles):
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
        if (self.pos in availableMovesDiagonal):
            availableMovesDiagonal.remove(self.pos)
        if (self.pos in availableMovesStraight):
            availableMovesStraight.remove(self.pos)
        if piecesDict[('black', 'white')[self.isWhite]][0].underCheck:
            return (self.checkForCheck(tilesList, piecesDict, piecesGridDict, self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMovesDiagonal)) | self.checkForCheck(tilesList, piecesDict, piecesGridDict, self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMovesStraight))) - toRemoveDiagonal - toRemoveStraight
        else:
            return (self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMovesDiagonal) | self.checkForPin(tilesList, piecesDict, piecesGridDict, availableMovesStraight)) - toRemoveDiagonal - toRemoveStraight

    # TODO: Queen's getAttackingTiles()
    def getAttackingTiles(self, tilesList, piecesDict):
        attackingTilesDiagonal = set()
        attackingTilesStraight = set()
        for x in range(1, 7):
            attackingTilesDiagonal.add((self.pos[0] - x, self.pos[1] - x))
            attackingTilesDiagonal.add((self.pos[0] - x, self.pos[1] + x))
            attackingTilesDiagonal.add((self.pos[0] + x, self.pos[1] - x))
            attackingTilesDiagonal.add((self.pos[0] + x, self.pos[1] + x))
            attackingTilesStraight.add((self.pos[0] - x, self.pos[1]))
            attackingTilesStraight.add((self.pos[0] + x, self.pos[1]))
            attackingTilesStraight.add((self.pos[0], self.pos[1] - x))
            attackingTilesStraight.add((self.pos[0], self.pos[1] + x))
        toRemoveDiagonal = set()
        toRemoveStraight = set()
        # Check for pieces in the way
        for i in piecesDict['white']:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1] and (i.name != 'King' or self.isWhite):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in attackingTilesDiagonal:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemoveDiagonal.add(x)
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]) and (i.name != 'King' or self.isWhite):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in attackingTilesStraight:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) >= 1):
                            toRemoveStraight.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) >= 1):
                            toRemoveStraight.add(x)
        for i in piecesDict['black']:
            if i.pos[0] != self.pos[0] and i.pos[1] != self.pos[1] and (i.name != 'King' or not self.isWhite):
                for x in attackingTilesDiagonal:
                    if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1 and (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1) and (x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) == (x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]):
                        toRemoveDiagonal.add(x)
            if i.pos != self.pos and (i.pos[0] == self.pos[0] or i.pos[1] == self.pos[1]) and (i.name != 'King' or not self.isWhite):
                # Add tiles that are behind the roadblock piece to toRemove
                for x in attackingTilesStraight:
                    if i.pos[0] == self.pos[0]:
                        if ((x[1] - self.pos[1]) / (i.pos[1] - self.pos[1]) > 1):
                            toRemoveStraight.add(x)
                    if i.pos[1] == self.pos[1]:
                        if ((x[0] - self.pos[0]) / (i.pos[0] - self.pos[0]) > 1):
                            toRemoveStraight.add(x)
        return (attackingTilesDiagonal | attackingTilesStraight) - toRemoveDiagonal - toRemoveStraight


class King(Piece):
    name = 'King'
    display = 'K'
    hasMoved = False

    def getAvailableMoves(self, tilesList, piecesDict, piecesGridDict, checkedTiles):
        availableMoves = set()
        # Check for castling
        if not self.hasMoved and not self.underCheck:
            if (self.pos[0] + 3, self.pos[1]) in piecesGridDict and piecesGridDict[(self.pos[0] + 3, self.pos[1])].name == 'Rook' and not piecesGridDict[(self.pos[0] + 3, self.pos[1])].hasMoved:
                if not ((self.pos[0] + 1, self.pos[1]) in piecesGridDict) and not ((self.pos[0] + 2, self.pos[1]) in piecesGridDict):
                    if not ((self.pos[0] + 1, self.pos[1]) in checkedTiles) and not ((self.pos[0] + 2, self.pos[1]) in checkedTiles):
                        availableMoves.add((self.pos[0] + 2, self.pos[1]))
            if (self.pos[0] - 4, self.pos[1]) in piecesGridDict and piecesGridDict[(self.pos[0] - 4, self.pos[1])].name == 'Rook' and not piecesGridDict[(self.pos[0] - 4, self.pos[1])].hasMoved:
                if not ((self.pos[0] - 1, self.pos[1]) in piecesGridDict) and not ((self.pos[0] - 2, self.pos[1]) in piecesGridDict) and not ((self.pos[0] - 3, self.pos[1]) in piecesGridDict):
                    if not ((self.pos[0] - 1, self.pos[1]) in checkedTiles) and not ((self.pos[0] - 2, self.pos[1]) in checkedTiles):
                        availableMoves.add((self.pos[0] - 2, self.pos[1]))
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
        for x in availableMoves:
            if x in checkedTiles:
                checkTiles.add(x)
        '''for i in piecesDict[('white', 'black')[self.isWhite]]:
            attackedTiles = i.getAttackingTiles(tilesList, piecesDict)
            for x in availableMoves:
                if x in attackedTiles:
                    checkTiles.add(x)
            availableMoves -= checkTiles'''
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

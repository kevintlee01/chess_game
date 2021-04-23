from Pieces import *
from CONST import *

class Player:
    def __init__(self, color):
        self.piecesAlive = []
        self.occupied = set()
        self.color = color.upper()
        self.initializePlayer()

    def initializePlayer(self):
        if self.color == "WHITE":
            for i in range(BOARD_SIZE):
                self.piecesAlive.append(Pawn("WHITE", (i, 1)))
            self.piecesAlive.extend([Castle("WHITE", (0, 0)), Castle("WHITE", (7, 0))])
            self.piecesAlive.extend([Knight("WHITE", (1, 0)), Knight("WHITE", (6, 0))])
            self.piecesAlive.extend([Bishop("WHITE", (2, 0)), Bishop("WHITE", (5, 0))])
            self.piecesAlive.append(Queen("WHITE", (3, 0)))
            self.piecesAlive.append(King("WHITE", (4, 0)))
        if self.color == "BLACK":
            for i in range(BOARD_SIZE):
                self.piecesAlive.append(Pawn("BLACK", (i, 6)))
            self.piecesAlive.extend([Castle("BLACK", (0, 7)), Castle("BLACK", (7, 7))])
            self.piecesAlive.extend([Knight("BLACK", (1, 7)), Knight("BLACK", (6, 7))])
            self.piecesAlive.extend([Bishop("BLACK", (2, 7)), Bishop("BLACK", (5, 7))])
            self.piecesAlive.append(Queen("BLACK", (3, 7)))
            self.piecesAlive.append(King("BLACK", (4, 7)))

    def getPiecesAlive(self):
        return self.piecesAlive

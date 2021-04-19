from Pieces import *

class Player:
    def __init__(self, color):
        self.piecesAlive = []
        self.color = color.upper()
        self.initializePlayer()

    def initializePlayer(self):
        if self.color == "WHITE":
            self.piecesAlive.extend([Pawn("WHITE", (0, 1)), Pawn("WHITE", (1, 1)), \
                                    Pawn("WHITE", (2, 1)), Pawn("WHITE", (3, 1)), \
                                    Pawn("WHITE", (4, 1)), Pawn("WHITE", (5, 1)), \
                                    Pawn("WHITE", (6, 1)), Pawn("WHITE", (7, 1))])
            self.piecesAlive.extend([Castle("WHITE", (0, 0)), Castle("WHITE", (7, 0))])
            self.piecesAlive.extend([Knight("WHITE", (1, 0)), Knight("WHITE", (6, 0))])
            self.piecesAlive.extend([Bishop("WHITE", (2, 0)), Bishop("WHITE", (5, 0))])
            self.piecesAlive.append(Queen("WHITE", (3, 0)))
            self.piecesAlive.append(King("WHITE", (4, 0)))
        if self.color == "BLACK":
            self.piecesAlive.extend([Pawn("BLACK", (0, 6)), Pawn("BLACK", (1, 6)), \
                                    Pawn("BLACK", (2, 6)), Pawn("BLACK", (3, 6)), \
                                    Pawn("BLACK", (4, 6)), Pawn("BLACK", (5, 6)), \
                                    Pawn("BLACK", (6, 6)), Pawn("BLACK", (7, 6))])
            self.piecesAlive.extend([Castle("BLACK", (0, 7)), Castle("BLACK", (7, 7))])
            self.piecesAlive.extend([Knight("BLACK", (1, 7)), Knight("BLACK", (6, 7))])
            self.piecesAlive.extend([Bishop("BLACK", (2, 7)), Bishop("BLACK", (5, 7))])
            self.piecesAlive.append(Queen("BLACK", (3, 7)))
            self.piecesAlive.append(King("BLACK", (4, 7)))

    def getPiecesAlive(self):
        return self.piecesAlive

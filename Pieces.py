from Piece import Piece
from CONST import *

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__("PAWN", color, position)

    def possibleMoves(self, board):
        positionList = []
        x, y = super().getPosition()

        if y+1 < BOARD_SIZE:
            #Pawn moves forward 1 step
            if board[y+1][x] == " ":
                positionList.append((x, y+1))

            #Pawn moves diagonal to take over opposite colored piece
            if x+1 < BOARD_SIZE:
                if board[y+1][x+1] != " " and board[y+1][x+1].getColor() != super().getColor():
                    positionList.append((x - 1, y + 1))
            if 0 >= x-1:
                if board[y+1][x-1] != " " and board[y+1][x-1].getColor() != super().getColor():
                    positionList.append((x - 1, y + 1))

        return positionList

class Castle(Piece):
    def __init__(self, color, position):
        super().__init__("CASTLE", color, position)

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__("KNIGHT", color, position)

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__("BISHOP", color, position)

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__("QUEEN", color, position)

class King(Piece):
    def __init__(self, color, position):
        super().__init__("KING", color, position)


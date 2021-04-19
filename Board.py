from Pieces import *
from Player import Player

class Board:
    def __init__(self):
        self.UNICODE = {
            'B_CHECKER': u'\u25FB',
            'B_PAWN': u'\u265F',
            'B_CASTLE': u'\u265C',
            'B_KNIGHT': u'\u265E',
            'B_BISHOP': u'\u265D',
            'B_KING': u'\u265A',
            'B_QUEEN': u'\u265B',
            'W_CHECKER': u'\u25FC',
            'W_PAWN': u'\u2659',
            'W_CASTLE': u'\u2656',
            'W_KNIGHT': u'\u2658',
            'W_BISHOP': u'\u2657',
            'W_KING': u'\u2654',
            'W_QUEEN': u'\u2655'
        }

        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.p1 = Player("WHITE")
        self.p2 = Player("BLACK")

    def setBoard(self):
        for piece in self.p1.getPiecesAlive():
            x, y = piece.getPosition()
            name = piece.getName()
            self.board[y][x] = self.UNICODE["W_" + name]

        for piece in self.p2.getPiecesAlive():
            x, y = piece.getPosition()
            name = piece.getName()
            self.board[y][x] = self.UNICODE["B_" + name]

    def drawBoard(self):
        print("\n")
        print('\t|_____|_____|_____|_____|_____|_____|_____|_____|')
        for i in range(len(self.board)-1, -1, -1):
            print("\t|     |     |     |     |     |     |     |     |")
            print("\t|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |".format(self.board[i][0], self.board[i][1], self.board[i][2], self.board[i][3], self.board[i][4], self.board[i][5], self.board[i][6], self.board[i][7]))
            print('\t|_____|_____|_____|_____|_____|_____|_____|_____|')
        print("\n")

board = Board()
board.setBoard()
board.drawBoard()
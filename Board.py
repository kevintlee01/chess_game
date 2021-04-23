from Pieces import *
from Player import Player
from CONST import *

class Board:
    def __init__(self):
        self.UNICODE = {
            'BLACKCHECKER': u'\u25FB',
            'BLACKPAWN': u'\u265F',
            'BLACKCASTLE': u'\u265C',
            'BLACKKNIGHT': u'\u265E',
            'BLACKBISHOP': u'\u265D',
            'BLACKKING': u'\u265A',
            'BLACKQUEEN': u'\u265B',
            'WHITECHECKER': u'\u25FC',
            'WHITEPAWN': u'\u2659',
            'WHITECASTLE': u'\u2656',
            'WHITEKNIGHT': u'\u2658',
            'WHITEBISHOP': u'\u2657',
            'WHITEKING': u'\u2654',
            'WHITEQUEEN': u'\u2655'
        }

        self.board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.p1 = Player("WHITE")
        self.p2 = Player("BLACK")

    def setBoard(self):
        for piece in self.p1.getPiecesAlive():
            x, y = piece.getPosition()
            self.board[y][x] = piece

        for piece in self.p2.getPiecesAlive():
            x, y = piece.getPosition()
            self.board[y][x] = piece

    def drawBoard(self):
        print("\n")
        print('\t|_____|_____|_____|_____|_____|_____|_____|_____|')
        for i in range(len(self.board)-1, -1, -1):
            print("\t|     |     |     |     |     |     |     |     |")
            p = []

            for j in range(BOARD_SIZE):
                p.append(self.UNICODE[self.board[i][j].getColor()+self.board[i][j].getName()] if self.board[i][j] != " " else " ")

            print("\t|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |".format(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
            print('\t|_____|_____|_____|_____|_____|_____|_____|_____|')
        print("\n")

board = Board()
board.setBoard()
board.drawBoard()
from Player import Player
from Board import Board

class Chess:
    def __init__(self):
        self.p1 = Player("WHITE")
        self.p2 = Player("BLACK")
        self.board = Board()

    def playGame(self):
        self.board.setPiecesToBoard(self.p1, self.p2)
        self.board.drawBoard()

if __name__ == "__main__":
    chess = Chess()
    chess.playGame()
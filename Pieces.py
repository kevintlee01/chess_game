from Piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__("PAWN", color, position)

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


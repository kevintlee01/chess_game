class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
        self.alive = True

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getPosition(self):
        return self.position

    def getAlive(self):
        return self.alive

    def setAlive(self, alive):
        self.alive = alive

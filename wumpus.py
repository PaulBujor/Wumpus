from character import Character


class Wumpus(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)
        self.isAlive = True

    def printPosition(self):
        return "Wumpus @ {}".format(super().printPosition())

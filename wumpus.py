from character import Character


class Wumpus(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)

    def printPosition(self):
        return "Wumpus @ {}".format(super().printPosition())

from character import Character


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.hasBullet = True

    def fireGun(self):
        self.hasBullet = False

    def printPosition(self):
        return "Player @ {}".format(super().printPosition())

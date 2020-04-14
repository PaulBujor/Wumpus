class Character:
    def __init__(self, x=1, y=1):
        self.__x = x
        self.__y = y

    def moveUp(self):
        self.__y -= 1

    def moveDown(self):
        self.__y += 1

    def moveLeft(self):
        self.__x -= 1

    def moveRight(self):
        self.__x += 1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

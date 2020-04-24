class Character:
    def __init__(self, x=1, y=1):
        self.__x = x
        self.__y = y
        self.isAlive = True

    def kill(self):
        self.isAlive = False

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

    def move(self, mina, cmd):
        if cmd.upper() == "UP":
            if mina[self.getY()-1][self.getX()] != 1:
                self.moveUp()
        elif cmd.upper() == "DOWN":
            if mina[self.getY()+1][self.getX()] != 1:
                self.moveDown()
        elif cmd.upper() == "LEFT":
            if mina[self.getY()][self.getX()-1] != 1:
                self.moveLeft()
        elif cmd.upper() == "RIGHT":
            if mina[self.getY()][self.getX()+1] != 1:
                self.moveRight()
        else:
            print("idiot")

    def printPosition(self):
        return "x: {} y: {}".format(self.getX(), self.getY())

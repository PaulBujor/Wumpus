from wumpus import Wumpus
from player import Player
import numpy as np
import random
import os


def randomPos(mina):
    randX = random.randrange(1, 7)
    randY = random.randrange(1, 7)
    while mina[randY][randX] == 1 or (randX == 1 and randY == 1):
        randX = random.randrange(1, 7)
        randY = random.randrange(1, 7)
    return randX, randY


def printMine(mina, player, wumpus):
    for i in range(7):
        for j in range(7):
            if mina[i][j] == 1:
                print("0", end=" ")
            else:
                if player.getX() == j and player.getY() == i:
                    print("P", end=" ")
                elif wumpus.getX() == j and wumpus.getY() == i:
                    print("W", end=" ")
                else:
                    print(" ", end=" ")
        print()


def startGame():
    mina = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]

    vizitat = np.zeros((7, 7), dtype=int)
    # print(vizitat)

    player = Player()

    wumpusPosition = randomPos(mina)
    wumpus = Wumpus(wumpusPosition[0], wumpusPosition[1])
    print(wumpus.printPosition())

    gameFinished = False

    print(player.printPosition())

    while not gameFinished:
        clear = lambda: os.system('cls')
        clear()
        printMine(mina, player, wumpus)
        cmd = input("Enter UP / DOWN / LEFT / RIGHT / EXIT: ")
        if cmd.upper() == "UP":
            if mina[player.getY()-1][player.getX()] == 0:
                player.moveUp()
        elif cmd.upper() == "DOWN":
            if mina[player.getY()+1][player.getX()] == 0:
                player.moveDown()
        elif cmd.upper() == "LEFT":
            if mina[player.getY()][player.getX()-1] == 0:
                player.moveLeft()
        elif cmd.upper() == "RIGHT":
            if mina[player.getY()][player.getX()+1] == 0:
                player.moveRight()
        elif cmd == "EXIT":
            gameFinished = True
        else:
            print("idiot")
        # print(player.printPosition())

    print("Game finished.")


if __name__ == '__main__':
    startGame()

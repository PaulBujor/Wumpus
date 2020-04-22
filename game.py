from wumpus import Wumpus
from player import Player
import numpy as np
import random
import os

movements = {1: "UP", 2: "RIGHT", 3: "DOWN", 4: "LEFT"}
gameFinished = False


def randomPos(mina):
    randX = random.randrange(1, 7)
    randY = random.randrange(1, 7)
    while mina[randY][randX] == 1 or (randX == 1 and randY == 1):
        randX = random.randrange(1, 7)
        randY = random.randrange(1, 7)
    return randX, randY


def moveCharacter(character, mina, cmd, wumpus = None):
    if cmd == "EXIT":
        globals()["gameFinished"] = True
    elif cmd.upper() == "SHOOT" and wumpus is not None:
        direction = input("Enter UP / DOWN / LEFT / RIGHT: ")
        #TODO if bullet is there
        playerY = character.getY()
        playerX = character.getX()
        bulletMap = mina
        bulletMap[wumpus.getY()][wumpus.getX()] = 2
        a = None
        if direction.upper() == "UP":
            a = bulletMap.T[playerX][playerY-1::-1]  # NORD
        elif direction.upper() == "DOWN":
            a = bulletMap.T[playerX][playerY+1::]  # SUD
        elif direction.upper() == "RIGHT":
            a = bulletMap[playerY][playerX+1::]  # EST
        elif direction.upper() == "LEFT":
            a = bulletMap[playerY][playerX-1::-1]  # VEST
        for x in a:
            if x == 2:
                wumpus.kill()
                print("Wumpus ded")
                break
            elif x == 1:
                print("Bullet ded")
                break

    else:
        character.move(mina, cmd)


def printMine(mina, player, wumpus, vizitat):
    for i in range(7):
        for j in range(7):
            if vizitat[i][j] == 1:
                if mina[i][j] == 1:
                    print("X", end=" ")
                else:
                    if player.getX() == j and player.getY() == i:
                        print("P", end=" ")
                    elif wumpus.getX() == j and wumpus.getY() == i:
                        print("W", end=" ")
                    else:
                        print(" ", end=" ")
            else:
                print("?", end=" ")
        print()


def startGame():
    mina = np.array([[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]])

    vizitat = np.zeros((7, 7), dtype=int)

    player = Player()

    wumpusPosition = randomPos(mina)
    wumpus = Wumpus(wumpusPosition[0], wumpusPosition[1])
    print(wumpus.printPosition())

    print(player.printPosition())

    while not globals()["gameFinished"]:
        # clear = lambda: os.system('cls')
        # clear()
        #TODO vizitate 3x3 iei pozitia la player si in zona 3x3 din jur pui vizitat[i][j] = 1
        printMine(mina, player, wumpus, vizitat)
        cmd = input("Enter UP / DOWN / LEFT / RIGHT / SHOOT / EXIT: ")
        moveCharacter(player, mina, cmd, wumpus)
        randomKey = random.randint(1, 4)
        moveCharacter(wumpus, mina, movements.get(randomKey))
        # TODO check random so wumpus doesn't go into wall
        # print(player.printPosition())

    print("Game finished.")


if __name__ == '__main__':
    startGame()

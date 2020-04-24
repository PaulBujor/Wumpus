from wumpus import Wumpus
from player import Player
import numpy as np
import random
import os

movements = {1: "UP", 2: "RIGHT", 3: "DOWN", 4: "LEFT"}
gameFinished = False


def randomPos(matrix):
    randX = random.randrange(1, 7)
    randY = random.randrange(1, 7)
    while (matrix[randY][randX] != 0) or (randX == 1 and randY == 1):  # find a place which is not occupied
        randX = random.randrange(1, 7)
        randY = random.randrange(1, 7)
    return randY, randX


def shootWeapon(player, wumpus, matrix):
    direction = input("Enter UP / DOWN / LEFT / RIGHT: ")
    if not player.hasBullet:
        print("You don't have ammo! Can't shoot")
    else:
        playerX = player.getX()
        playerY = player.getY()
        bulletMap = matrix
        bulletMap[wumpus.getY()][wumpus.getX()] = 2
        a = None
        if direction.upper() == "UP":
            a = bulletMap.T[playerX][playerY - 1::-1]  # NORD
        elif direction.upper() == "DOWN":
            a = bulletMap.T[playerX][playerY + 1::]  # SUD
        elif direction.upper() == "RIGHT":
            a = bulletMap[playerY][playerX + 1::]  # EST
        elif direction.upper() == "LEFT":
            a = bulletMap[playerY][playerX - 1::-1]  # VEST

        for i in a:
            if i == 2:
                wumpus.kill()
                print("Arrrgghhhh i don't want to die -> Wumpus dead")
                break
            elif i == 1:
                print("You missed the shot!! -> Wall was hit")
                break
        player.fireGun()


def moveCharacter(character, matrix, cmd, wumpus=None):
    if cmd.upper() == "EXIT":
        globals()["gameFinished"] = True
    elif cmd.upper() == "SHOOT" and wumpus is not None:
        shootWeapon(character, wumpus, matrix)
    else:
        character.move(matrix, cmd)


def wumpusNear(player, wumpus):
    return (player.getX() - 1 == wumpus.getX() and player.getY() == wumpus.getY()) or (
            player.getX() + 1 == wumpus.getX() and player.getY() == wumpus.getY()) or (
                   player.getX() == wumpus.getX() and player.getY() + 1 == wumpus.getY()) or (
                   player.getX() == wumpus.getX() and player.getY() - 1 == wumpus.getY())


def checkPosition(player, wumpus, map):
    player.isAlive = not ((player.getX() == wumpus.getX() and player.getY() == wumpus.getY() and wumpus.isAlive) or
                          map[player.getY()][
                              player.getX()] == 3)


def printMine(map, player, wumpus, vizitat):
    for i in range(7):
        for j in range(7):
            if vizitat[i][j] == 1:
                if map[i][j] == 1:
                    print("X", end=" ")
                else:
                    if player.getX() == j and player.getY() == i:
                        print("P", end=" ")
                    # elif wumpus.getX() == j and wumpus.getY() == i:
                    #     print("W", end=" ")
                    elif map[i][j] == 5:
                        print("A", end=" ")
                    elif map[i][j] == 3:
                        print("B", end=" ")
                    elif wumpusNear(player, wumpus) and i == wumpus.getY() and j == wumpus.getX() and wumpus.isAlive:
                        print("S", end=" ")  # Stink
                    else:
                        print(" ", end=" ")
            else:
                print("?", end=" ")
        print()


def startGame():
    map = np.array([[1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1, 1, 1],
                    [1, 1, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1]])

    vizitat = np.zeros((7, 7), dtype=int)

    player = Player()

    wumpusPosition = randomPos(map)
    wumpus = Wumpus(wumpusPosition[0], wumpusPosition[1])

    numberOfPits = 2
    for i in range(numberOfPits):
        pitPosition = randomPos(map)
        map[pitPosition[0]][pitPosition[1]] = 3

    goldPosition = randomPos(map)
    map[goldPosition[0]][goldPosition[1]] = 5
    goldFound = False

    while not globals()["gameFinished"] and player.isAlive:
        os.system('cls')
        # visit
        vizitat[player.getY() - 1][player.getX()] = 1
        vizitat[player.getY() + 1][player.getX()] = 1
        vizitat[player.getY()][player.getX() - 1] = 1
        vizitat[player.getY()][player.getX() + 1] = 1
        vizitat[player.getY()][player.getX()] = 1

        printMine(map, player, wumpus, vizitat)
        cmd = input("Enter UP / DOWN / LEFT / RIGHT / SHOOT / EXIT: ")
        moveCharacter(player, map, cmd, wumpus)

        if player.getX() == goldPosition[1] and player.getY() == goldPosition[0]:
            print(
                "You have found the treasure. Now go back to where your started. Watch out! The Wumpus might be close!")
            goldFound = True
            map[goldPosition[0]][goldPosition[1]] = 0

        checkPosition(player, wumpus, map)

        randomKey = random.randint(1, 4)
        moveCharacter(wumpus, map, movements.get(randomKey))
        # TODO check random so wumpus doesn't go into wall
        # print(player.printPosition())

        if player.getY() == 1 and player.getX() == 1 and goldFound:
            globals()["gameFinished"] = True

    os.system('cls')
    printMine(map, player, wumpus, vizitat)
    print("Game finished.")
    if goldFound and player.isAlive:
        print("You won, you are jmen!")
    else:
        print("You're Hammond!")


if __name__ == '__main__':
    startGame()

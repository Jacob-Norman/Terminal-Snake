from random import randint
from math import floor

def setSnake(currentSnake: list[tuple], newHead: tuple, addTail: bool):
    newSnake: list[tuple] = []
    snakePositions = set()
    bodyTemp = newHead
    for body in currentSnake:
        newSnake.append(bodyTemp)
        snakePositions.add(bodyTemp)
        bodyTemp = body
    if addTail:
        newSnake.append(bodyTemp)
        snakePositions.add(bodyTemp)
    # newSnake will be used for determining movement and snakePositions will be used
    # to draw the snake on the board
    return newSnake, snakePositions

def setApple(snake: list[tuple]):
    potentialApple: list[int] = []
    for i in range((19 * 24)):
        potentialApple.append(i)
    for pos in snake:
        index = (ord(pos[0]) - 97) * 24 + pos[1]
        potentialApple.remove(index)
    # potentialApple is now all the squares in index from without a snake in it
    appleIndex = potentialApple[randint(0, (len(potentialApple) - 1))]
    appleRow = chr((floor(appleIndex/24)) + 97)
    appleCol = appleIndex % 24 
    return (appleRow, appleCol)
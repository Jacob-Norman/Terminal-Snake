import board
import snakeApple as snapple
from time import sleep
import keyboard as keys
import msvcrt

def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()

validRow = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'}
validCol = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
            15, 16, 17, 18, 19, 20, 21, 22, 23}

# If this function is exited without the program terminating then the player is ready to play
def startMenu(stdscr):
    response = ''
    while response != "p" or response != "q":
        board.printEmptyFrame(stdscr)
        stdscr.addstr(21, 0,"           Play [p]           Quit[q]\n")
        stdscr.refresh()
        flush_input()
        response = stdscr.getkey()
        if response == "p":
            stdscr.clear()
            stdscr.refresh()
            break
        elif response == "q":
            exit()
        else:
            stdscr.addstr(22, 0, f"You entered {response}\nPlease enter either 'p' or 'q'")
            stdscr.refresh()
            sleep(2)
    return 0

def moveSnake(currentHead: tuple, prevDir: str):
    newDir = str()
    oppDir = str()
    if keys.is_pressed('w') or keys.is_pressed("up"):
        newDir = "up"
        oppDir = "down"
    elif keys.is_pressed('a') or keys.is_pressed("left"):
        newDir = "left"
        oppDir = "right"
    elif keys.is_pressed('s') or keys.is_pressed("down"):
        newDir = "down"
        oppDir = "up"
    elif keys.is_pressed('d') or keys.is_pressed("right"):
        newDir = "right"
        oppDir = "left"
    else:
        newDir = prevDir
        oppDir = ''

    # If user tries to go in the opposite direction then they will keep going the same way
    if prevDir == oppDir:
        newDir = prevDir
    
    if newDir == "up":
        newHead = (chr(ord(currentHead[0]) - 1), currentHead[1])
    elif newDir == "down":
        newHead = (chr(ord(currentHead[0]) + 1), currentHead[1])
    elif newDir == "left":
        newHead = (currentHead[0], currentHead[1] - 1)
    elif newDir == "right":
        newHead = (currentHead[0], currentHead[1] + 1)
    
    return (newHead, newDir)

def gameMain(stdscr):
    #starting values of the game
    snake: list[tuple] = [('j', 15),('j', 16), ('j', 17), ('j', 18), ('j', 19)]
    snakePosition: set[tuple] = {('j', 15),('j', 16), ('j', 17), ('j', 18), ('j', 19)}
    apple: tuple = ('j', 5)
    direction: str = "left"
    head: tuple = ('j', 15)
    ateApple: bool = False
    while True:
        #check for apple
        if apple in snakePosition:
            ateApple = True
        
        #determine snake position
        head, direction = moveSnake(head, direction)
        if head in snakePosition:
            break
        (snake, snakePosition) = snapple.setSnake(snake, head, ateApple)
        if not(head[0] in validRow) or not(head[1] in validCol):
            break

        #regenerate the apple
        if ateApple:
            apple = snapple.setApple(snake)
            ateApple = False

        #draw game
        frame = board.drawFrame(snakePosition, apple) 
        board.printFrame(stdscr, frame)

        #delay
        sleep(0.08)

def gameOver(stdscr):
    response = ''
    while response != 'r' or response != 'q':
        board.printGameOver(stdscr)
        flush_input()
        response = stdscr.getkey()
        if response == 'q':
            retry = False
            return retry
        elif response == 'r':
            retry = True
            return retry
        else:
            stdscr.addstr(22, 0, f"You entered {response}\nPlease enter either 'p' or 'q'")
            stdscr.refresh()
            sleep(2)
import game
import time

from curses import wrapper

def main(stdscr):
    retry = True
    game.startMenu(stdscr)
    highScore: int = 0
    while retry:
        score = game.gameMain(stdscr)
        if score > highScore:
            highScore = score
        time.sleep(1)
        retry = game.gameOver(stdscr, score, highScore)

wrapper(main)
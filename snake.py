import game
import time

from curses import wrapper

def main(stdscr):
    retry = True
    game.startMenu(stdscr)

    while retry:
        game.gameMain(stdscr)
        time.sleep(1)
        retry = game.gameOver(stdscr)

wrapper(main)
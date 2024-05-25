import game
import time

retry = True
game.startMenu()

while retry:
    game.gameMain()
    time.sleep(1)
    retry = game.gameOver()

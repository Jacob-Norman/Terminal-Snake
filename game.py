from board import printEmptyFrame
from time import sleep

# If this function is exited without the program terminating then the player is ready to play
def startMenu():
    response = ''
    while response != "y" or response != "q":
        printEmptyFrame()
        response = input("Please adjust your terminal size so that the entire board is visible.\nIf you are ready to play, type 'y' if you would like to quit type 'q': ")
        response.lower()
        if response == "y":
            break
        elif response == "q":
            exit()
        else:
            print("Please enter either 'y' or 'q'")
            sleep(1.5)
    return 0
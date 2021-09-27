from gameboard import GameBoard
from player import Player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = GameBoard()

# Create a new Player called played starting at position 3,2
played = Player(3, 2)

while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")
    
    # TODO
    # Move the player through the board
    if selection == "w" and board.checkMove(played.rowPosition -1, played.columnPosition): 
        played.moveUp()
    elif selection == "s" and board.checkMove(played.rowPosition +1, played.columnPosition):
        played.moveDown()
    elif selection == "a" and board.checkMove(played.rowPosition, played.columnPosition -1):
        played.moveLeft()
    elif selection == "d" and board.checkMove(played.rowPosition, played.columnPosition +1):
        played.moveRight()
    else:
        print("Wrong input!")

    # Check if the player has won, if so print a message and break the loop!
    if board.checkWin(played.rowPosition, played.columnPosition):
        print("Winner!")
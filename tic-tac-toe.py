#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    if position in board:
        if board[position] == ' ':
            board[position] = mark
            return True
        else:
            return False
    else:
        return False

# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    newPrintboard = []
    for i in board:
        newPrintboard.append(str(board[i]).replace(' ', str(i)))        
    
    print(newPrintboard[0] + ' | ' + newPrintboard[1] + ' | ' + newPrintboard[2])
    print('---------')
    print(newPrintboard[3] + ' | ' + newPrintboard[4] + ' | ' + newPrintboard[5])
    print('---------')
    print(newPrintboard[6] + ' | ' + newPrintboard[7] + ' | ' + newPrintboard[8])

# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    position = int(position)
    if 1 <= position <= 9:
        if board[position] == ' ':
            return True
        else:
            return False
    return False

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9],  
    [1, 4, 7], 
    [2, 5, 8], 
    [3, 6, 9],  
    [1, 5, 9], 
    [3, 5, 7] 
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for com in winCombinations:
        if all(board[position] == player for position in com):
               return True
    return False

# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for position in board.values():
        if position == ' ':
            return False
    else:
        return True

#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while True:
    gameEnded = False
    currentTurnPlayer = 'X'
    
    while not gameEnded:
        move = input("\n" + currentTurnPlayer + "'s turn, input: ")
        
        if move in '1 2 3 4 5 6 7 8 9'.split():
            move = int(move)
            if 1 <= move <= 9:
                if validateMove(move):
                    markBoard(move, currentTurnPlayer)
                    print('\n')
                    printBoard()
                    if checkWin(currentTurnPlayer):
                        print(f"\nPlayer {currentTurnPlayer} wins!")
                        gameEnded = True
                    elif checkFull():
                        print("\nGame over! The match is tied.")
                        gameEnded = True
                    else:
                        currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'
                else:
                    print("Position's already occupied! Please try another one.")
            else:
                print("Invalid input! Please submit a number between 1-9.")
        else:
            print("Invalid input! Please submit a number between 1-9.")
 

    playAgain = input("\nDo you want to play again? (y/n): ")
    if playAgain == "y" or playAgain == "Y":
        for key in board:
            board[key] = ' '
        print('\nNew game started:\n')
        printBoard()
    else:
        print("Thanks for playing!")
        break



# Bonus Point: Implement the feature for the user to restart the game after a tie or game over

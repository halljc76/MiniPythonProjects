import copy
import random

"""
Update Jun 10th: Continue debugging computer's setup method.
                 Make the blank boards serve as 'overlaps' for the actual compuer board.
                 Make sure the program marks ALL computer hits.
"""

hasWon = False
rows = [1,2,3,4,5]
columns = [1,2,3,4,5]


def board():
    return [" "] * 25

def playerConfigure(player_board):
    
    remainingPositions = [(i, j) for i in rows for j in columns]
    takenPositions = []
    
    
    lengths = [1,1,2,3]
    ships = ["S", "S", "D", "B"]
    shipNames = ["Submarine", "Submarine", "Destroyer", "Battleship"]
    
    print("Player, set up your board.")
    for i in range(len(lengths)):
        rowChosen = False
        colChosen = False
        rotatedBoolean = False

        if lengths[i] != 1:
            rotated = input("Please input 'Yes' or 'No' if you [do not] want your " + shipNames[i] + "  rotated.")
            while rotated not in ["Yes", "No", "yes", "no"]:
                print("You did not select a valid option.")
                rotated = input("Please input 'Yes' or 'No' if you [do not] want your " + shipNames[i] + " rotated.")
            
            if rotated == "Yes" or rotated == "yes":
                rotatedBoolean = True
        
        elif lengths[i] == 1:
            print("Placing a submarine.")
        
        while not rowChosen:
            try:
                row = input("Please enter an integer 1-5 for the row.")
                row = int(row)
            except TypeError:
                print("You did not select an integer.")
            
            print(row in rows)
            print(row + lengths[i] - 1) 
            print(rotatedBoolean)
            
            if row not in rows or ((row + lengths[i] - 1 > 5) and rotatedBoolean):
                print("You did not select a valid integer.")
            
            else:
                rowChosen = True
        
        
        while not colChosen:
            try:
                col = input("Please enter an integer 1-5 for the column.")
                col = int(col)
            except TypeError:
                print("You did not select an integer.")

            if (col not in columns) or ((col + lengths[i] - 1 > 5) and not rotatedBoolean):
                print("You did not select a valid integer.")
            
            else:
                colChosen = True
        
        if (row, col) in takenPositions:
            print("You have selected an occupied position.")
            print("Randomly placing your ship...")
            tempRows = []
            tempCols = []
            for num in rows:
                if num != row:
                    tempRows.append(num)
            
            for num in columns:
                if num != col:
                    tempCols.append(num)
            

            row = random.choice(tempRows)
            col = random.choice(tempRows)
        
        start = (5 * (row - 1)) + (col - 1) 
        player_board[start] = ships[i]
        for j in range(1,lengths[i]):
            
            if lengths[i] != 1:
                if rotatedBoolean:
                    player_board[start + 5] = ships[i]
                    start = start + 5
                else:
                    player_board[start + 1] = ships[i]
                    start = start + 1
        
        remainingPositions.remove((row, col))
        takenPositions.append((row, col))

        print("1 2 3 4 5")
        for i in range(0,5):
            print(player_board[(5 * i)], player_board[(5 * i) + 1], player_board[(5 * i) + 2], 
            player_board[(5 * i) + 3], player_board[(5 * i) + 4], "   " + str(i + 1))
        
    return player_board, takenPositions

def computerConfigure(computer_board):
    remainingPositions = [(i, j) for i in rows for j in columns]
    takenPositions = []
    validPositionFound = False

    lengths = [1,1,2,3]
    ships = ["S", "S", "D", "B"]
    
    print("The computer will now set up its board.")
    for i in range(len(lengths)):
        rotateOrNot = random.choice([True, False])
        
        while not validPositionFound:        
            randPosition = random.choice(remainingPositions)
            print(randPosition)
            print(remainingPositions)
            randRow = randPosition[0]
            randCol = randPosition[1]

            if ((randRow + lengths[i] - 1 > 5) and rotateOrNot) or ((randCol + lengths[i] - 1 > 5) and not rotateOrNot):
                pass
            else:
                validPositionFound = True

        print(randPosition in remainingPositions)
        newRemaining = [] # Continued receiving error with remove function here. Had to make a workaround.
        for position in remainingPositions:
            if position != randPosition:
                newRemaining.append(position)
        remainingPositions = newRemaining
        takenPositions.append(randPosition)

        

        start = (5 * (randRow - 1)) + (randCol - 1) 
        computer_board[start] = ships[i]
        for j in range(1,lengths[i]):
            
            if lengths[i] != 1:
                if rotateOrNot:
                    print(i)
                    print("List loc: ", start + 5)
                    computer_board[start + 5] = ships[i]
                    start = start + 5
                else:
                    computer_board[start + 1] = ships[i]
                    start = start + 1


    return computer_board, takenPositions

def playerMove(computer_board, computer_positions):
    remainingPositions = [(i, j) for i in rows for j in columns]
    calledPositions = []

    while True:
        try:
            row = input("Please input a row coordinate (1-5).")
            row = int(row)

            col = input("Please input a column coordinate (1-5).")
            col = int(col)
        except TypeError or row not in rows or col not in columns or (row, col) in calledPositions:
            print("Player, either you selected an invalid row or column, or that position has already been called.")
        
        position = (row, col)
        if position in computer_positions:
            print("Hit!")
            computer_board[(5 * (position[0] - 1)) + position[1] - 1] = "X"

            print("1 2 3 4 5")
            for i in range(0,5):
                print(computer_board[(5 * i)], computer_board[(5 * i) + 1], computer_board[(5 * i) + 2], 
                computer_board[(5 * i) + 3], computer_board[(5 * i) + 4], "   " + str(i + 1))
        else:
            computer_board[(5 * (position[0] - 1)) + position[1] - 1] = "O"
            print("Miss.")
            break

def computerMove(player_board, player_positions):
    remainingPositions = [(i, j) for i in rows for j in columns]
    calledPositions = []

    while True:
        randPosition = random.choice(remainingPositions)
        remainingPositions.remove(randPosition)
        calledPositions.append(randPosition)

        if randPosition in player_positions:
            print("Computer has landed a hit!")
            player_board[(5 * (randPosition[0] - 1) + (randPosition[1] - 1))] = "X"
            for i in range(0,5):
                print(player_board[(5 * i)], player_board[(5 * i) + 1], player_board[(5 * i) + 2], 
                player_board[(5 * i) + 3], player_board[(5 * i) + 4], "   " + str(i + 1))
        else:
            print("Computer has missed the ships.")
            player_board[(5 * (randPosition[0] - 1) + (randPosition[1] - 1))] = "O"
            break

def checkSunkOrWin(playerOrComputer, board):
    numSub = 0
    numDest = 0
    numBattle = 0

    for i in range(len(board)):
        if board[i] == "S":
            numSub += 1
        elif board[i] == "D":
            numDest += 1
        elif board[i] == "B":
            numBattle += 1
        
    # Replace with np.count_nonzero() later.
    if (numSub == -1) and (numDest == -1) and (numBattle == -1):
        hasWon = True
        return "The " + str(playerOrComputer) + "has won the game!"
    elif (numSub == 0):
        numSub == -1
    elif (numDest == 0):
        numDest == -1
    elif (numBattle == 0):
        numBattle == -1

def main():
    print("Welcome to Battleship!")
    print("Here, you will face against a randomized computer player. The object is to first sink all opposing ships!")
    print("For each turn, the player will see an 'X' denoting a hit and a 'O' denoting a miss.")

    blank_board = board()
    blank_board2 = board()
    player_board, player_positions = playerConfigure(blank_board)
    computer_board, computer_positions = computerConfigure(blank_board2)
    while not hasWon:
        playerMove(computer_board, computer_positions)
        checkSunkOrWin("Player", computer_board)
        computerMove(player_board, player_positions)
        checkSunkOrWin("Computer", player_board)

if __name__ == "__main__":
    main()

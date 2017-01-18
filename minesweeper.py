from random import randint

board = []
row = 6
col = 7
mine_count = 5
""" Use when done testing
row = int(input("# of rows: "))
col = int(input("# of columns: "))
mine_count = int(input("# of mines: "))
"""
answers = []

#creates board
for x in range(0, row):
    board.append(["?"] * col)

#prints board
def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

#picks random coordinate for row
def rand_row(board):
    return randint(0, len(board) - 1)

#picks random coordinate for column
def rand_col(board):
    return randint(0, len(board[0]) - 1)

#adding mine coordinate to list of answers
for x in range(0,mine_count):
    mine_row = rand_row(board)
    mine_col = rand_col(board)
    answers.append({mine_row,mine_col})
#for testing purposes only - hide when finished
def printAnswers():
    for answer in answers:
        print(answer)
printAnswers()

while(True):
    #restrict guesses to be within board
    guess_row = int(input("Guess Row:"))
    while guess_row < 0 or guess_row > row - 1:
        guess_row = int(input("That's not even on the board! Guess Row: "))
        
    guess_col = int(input("Guess Col:"))
    while guess_col < 0 or guess_col > col - 1:
        guess_col = int(input("That's not even on the board! Guess Col: "))
    
    #used in perim
    def is_mine(r, c):
        if {c, r} in answers:
            return True
        else:
            return False       
                   
    def perim(r, c):
        count = 0
        if r == 0:
            #no r-1
            if c == 0:
                #no c-1
                if is_mine(r, c + 1):
                    count += 1
                if is_mine(r + 1, c):
                    count += 1
                if is_mine(r + 1, c + 1):
                    count += 1
            elif c == (col - 1):
                #no c+1
                if is_mine(r, c - 1):
                    count += 1
                if is_mine(r + 1, c - 1):
                    count += 1
                if is_mine(r + 1, c):
                    count += 1
        elif r == (row - 1):
            #no r+1
            if c == 0:
                #no c-1
                if is_mine(r - 1, c):
                    count += 1
                if is_mine(r - 1, c + 1):
                    count += 1
                if is_mine(r, c + 1):
                    count += 1
            elif c == (col - 1):
                #no c+1
                if is_mine(r - 1, c - 1):
                    count += 1
                if is_mine(r - 1, c):
                    count += 1
                if is_mine(r, c - 1):
                    count += 1
        else:
            #no restriction
            if is_mine(r - 1, c - 1):
                count += 1
            if is_mine(r - 1, c):
                count += 1
            if is_mine(r - 1, c + 1):
                count += 1
            if is_mine(r, c - 1):
                count += 1
            if is_mine(r, c + 1):
                count += 1
            if is_mine(r + 1, c - 1):
                count += 1
            if is_mine(r + 1, c):
                count += 1
            if is_mine(r + 1, c + 1):
                count += 1
        board[r][c] = str(count)
    #if you guess directly on a mine's position
    if {guess_row, guess_col} in answers:
        print("GAME OVER")
        #checks for all coordinates in list 'answers' and sets them to "X" from "?"
        for columns in range(len(board[0])):
            for rows in range(len(board)):
                if {rows, columns} in answers:    
                    board[rows][columns] = "X"
        print_board(board)
        
    else:
        perim(guess_row, guess_col)
        print_board(board)
        

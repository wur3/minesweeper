from random import randint
import random
random.seed(1)
board = []
row = 10
col = 10
mine_count = 4
""" Use when done testing
row = int(input("# of rows: "))
col = int(input("# of columns: "))
mine_count = int(input("# of mines: "))
"""
answers = []
checked = []

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
    #print(str(mine_row)+" "+str(mine_col))
    answers.append({mine_row, mine_col})
#for testing purposes only - hide when finished
def printAnswers():
    for answer in answers:
        print(answer)
printAnswers()

turn = 1
keepGoing = True
while(keepGoing):
    print("\nTurn " + str(turn) + "---------------")
    #restrict guesses to be within board
    guess_row = int(input("Guess Row: "))
    while guess_row < 0 or guess_row > row - 1:
        guess_row = int(input("That's not even on the board! Guess Row: "))
    
    guess_col = int(input("Guess Col: "))
    while guess_col < 0 or guess_col > col - 1:
        guess_col = int(input("That's not even on the board! Guess Col: "))
    
    if {guess_row, guess_col} in checked:
        print("That point was already checked!")
    
    def is_mine(r, c):
        if {r, c} in answers:
            return True
        else:
            return False
    def within(r, c):
        if r < 0 or r > row - 1:
            return False
        if c < 0 or c > col - 1:
            return False
        return True
    
    def search(r, c):
        if not within(r, c): #if out of bounds
            return
        
        if {r, c} in checked: #if already checked
            return
        
        if is_mine(r, c): #if a mine
            return
        
        if perim(r, c) > 0: #it is adjacent to at least one mine
            board[r][c] = str(perim(r, c))
            return
        else:
            board[r][c] = " "
        
        if {r, c} not in checked:
            checked.append({r, c})
        print(r, c, " checked and is set to ", str(perim(r, c)))
        
        for (dr, dc) in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
            search(dr, dc)          
            
    def perim(r, c):
        count = 0
        for (dr, dc) in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
            if within(dr, dc) and is_mine(dr, dc):
                count += 1
        return count
    
    #if you guess directly on a mine's position
    if {guess_row, guess_col} in answers:
        print("GAME OVER")
        #checks for all coordinates in list 'answers' and sets them to "X" from "?"
        for columns in range(len(board[0])):
            for rows in range(len(board)):
                if {rows, columns} in answers:    
                    board[rows][columns] = "X"
        print_board(board)
        keepGoing = False
    else:
        search(guess_row, guess_col)
        print_board(board)
    turn += 1 

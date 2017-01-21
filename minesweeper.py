from random import randint
import random
random.seed(1)

row = 10
col = 10
mine_count = 4
""" Use when done testing
row = int(input("# of rows: "))
col = int(input("# of columns: "))
mine_count = int(input("# of mines: "))
"""

checked = []

#creates board
board = [["?" for x in range(col)] for y in range(row)] 
answer = [["0" for x in range(col)] for y in range(row)] 

#prints board
def print_board():
    for row in board:
        print(" ".join(row))
print_board()

#prints answer
def print_answer():
    for row in answer:
        print(" ".join(row))

#picks random coordinate for row
def rand_row(board):
    return randint(0, len(board) - 1)

#picks random coordinate for column
def rand_col(board):
    return randint(0, len(board[0]) - 1)

#adding mines to answer
for x in range(0,mine_count):
    mine_row = rand_row(board)
    mine_col = rand_col(board)
    answer[mine_row][mine_col] = "X"
    
print_answer()
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
        if {r, c} in answer:
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
        
        for (dr, dc) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c+1), (r+1, c-1), (r-1, c-1)]:
            search(dr, dc)
            
    def perim(r, c):
        count = 0
        for (dr, dc) in [(r, c+1), (r, c-1), (r+1, c), (r-1, c), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)]:
            if within(dr, dc) and is_mine(dr, dc):
                count += 1
        return count
    
    #if you guess directly on a mine's position
    if answer[guess_row][guess_col]=="X":
        print("GAME OVER")
        #checks for all coordinates in list 'answer' and sets them to "X" from "?"
        for columns in range(len(board[0])):
            for rows in range(len(board)):
                if {rows, columns} in answer:    
                    board[rows][columns] = "X"
        print_answer()
        keepGoing = False
    else:
        search(guess_row, guess_col)
        print_board()
    turn += 1 

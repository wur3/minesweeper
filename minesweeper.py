from random import randint
import random
"""
random.seed(1)

row = 10
col = 10
mine_count = 4
"""
row = int(input("# of rows: "))
col = int(input("# of columns: "))
mine_count = int(input("# of mines: "))

spaces_left = row * col - mine_count

#creates board that is displayed to user
board = [["?" for x in range(col)] for y in range(row)] 

#creates behind the scenes grid: 0=unchecked coordinates, 1=checked coordinates, X=mines
bts = [["0" for x in range(col)] for y in range(row)] 

#prints board: entering True as the parameter reveals mines
def print_board(reveal = False):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if(bts[row][col]=='X' and reveal == True):
                print(" ".join('X'), end=' ')
            else:
                print(" ".join(board[row][col]), end=' ')
        print()

#prints bts
def print_bts():
    for row in range(len(bts)):
        for col in range(len(bts[row])):
            print(" ".join(bts[row][col]), end=' ')
        print()

#picks random coordinate for row
def rand_row(board):
    return randint(0, len(board) - 1)

#picks random coordinate for column
def rand_col(board):
    return randint(0, len(board[0]) - 1)

#adding mines to bts
for x in range(0, mine_count):
    mine_row = rand_row(board)
    mine_col = rand_col(board)
    bts[mine_row][mine_col] = "X"

turn = 1
keepGoing = True

while(keepGoing):
    print("\nTurn " + str(turn) + "--------------------------------------")
    print_board()
    #restrict guesses to be within board
    guess_row = int(input("\nGuess Row: "))
    while guess_row < 0 or guess_row > row - 1:
        guess_row = int(input("That's not even on the board! Guess Row: "))
    
    guess_col = int(input("Guess Col: "))
    while guess_col < 0 or guess_col > col - 1:
        guess_col = int(input("That's not even on the board! Guess Col: "))
    
    def is_mine(r, c):
        if bts[r][c]=="X":
            return True
        else:
            bts[r][c]="1"
            return False
    def within(r, c):
        if r < 0 or r > row - 1:
            return False
        if c < 0 or c > col - 1:
            return False
        return True
    
    def search(r, c):
        if not within(r, c): #if out of bounds
            #print(r, c, " is out of bounds")
            return
        
        if not board[r][c]=="?": #if already checked
            #print(r, c, " is not ?")
            return
        
        if is_mine(r, c): #if a mine
            #print(r, c, " is a mine")
            return
        global spaces_left
        spaces_left-=1
        if perim(r, c) > 0: #it is adjacent to at least one mine
            board[r][c] = str(perim(r, c))
            #print(r, c, " has an adjacent mine")
            return
        else:
            board[r][c] = "_"
            
            for (dr, dc) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c+1), (r+1, c-1), (r-1, c-1)]:
                search(dr, dc)
            
    def perim(r, c):
        count = 0
        for (dr, dc) in [(r, c+1), (r, c-1), (r+1, c), (r-1, c), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)]:
            if within(dr, dc) and is_mine(dr, dc):
                count += 1
        return count
    
    #if you guess directly on a mine's position
    if bts[guess_row][guess_col]=="X":
        print("\nGAME OVER\n")
        print_board(True)
        keepGoing = False
    else:
        search(guess_row, guess_col)
        if(spaces_left == 0):
            print("\nCONGRATULATIONS! You win!\n")
            print_board(True)
            keepGoing = False

    turn += 1 
print("------------------GAME END------------------")
